import globals
import random
import tkinter as tk
from tkinter import Scrollbar, ttk
from math import *
from figure_types import *
from canvas import *
from collections import OrderedDict
from time import time


class AutoScrollbar(ttk.Scrollbar):

    """A scrollbar that hides itself if it's not needed.
    Works only if you use the grid geometry manager"""

    def set(self, lo, hi):
        if float(lo) <= 0.0 and float(hi) >= 1.0:
            self.grid_remove()
        else:
            self.grid()
            ttk.Scrollbar.set(self, lo, hi)

    def pack(self, **kw):
        raise tk.TclError("Cannot use pack with this widget")

    def place(self, **kw):
        raise tk.TclError("Cannot use place with this widget")


class UI:

    """Provides zoom of the canvas"""

    def __init__(self, mainframe, width=600, height=400):
        """Initialize the UI"""

        # Vertical and horizontal scrollbars for canvas

        vbar = AutoScrollbar(mainframe, orient="vertical")
        hbar = AutoScrollbar(mainframe, orient="horizontal")

        self.scrollbars = []

        # Create canvas

        self.canvas = xCanvas(
            mainframe,
            highlightthickness=0,
            width=width,
            height=height,
        )
        self.canvas.update()  # wait till canvas is created
        # bind scrollbars to the canvas
        vbar.configure(command=self.__scroll_y)
        hbar.configure(command=self.__scroll_x)

        # Bind events to the Canvas

        self.delta = 1.25  # zoom magnitude
        self.canvas.bind("<Configure>", self.canvas.show)  # canvas is resized
        self.canvas.bind("<ButtonPress-1>", self.__move_from)
        self.canvas.bind("<B1-Motion>", self.__move_to)
        # zoom for Windows and MacOS, but not Linux
        self.canvas.bind("<MouseWheel>", self.__wheel)
        # only with Linux, __wheel scroll down
        self.canvas.bind("<Button-5>", self.__wheel)
        # only with Linux, __wheel scroll up
        self.canvas.bind("<Button-4>", self.__wheel)

        self.redraw()

    def __scroll_y(self, *args, **kwargs):
        """Scroll canvas vertically and redraw the image"""

        self.canvas.yview(*args, **kwargs)  # scroll vertically
        self.redraw()  # redraw the image

    def __scroll_x(self, *args, **kwargs):
        """Scroll canvas horizontally and redraw the image"""

        self.canvas.xview(*args, **kwargs)  # scroll horizontally
        self.redraw()  # redraw the image

    def __move_from(self, event):
        """Remember previous coordinates for scrolling with the mouse"""

        self.canvas.scan_mark(event.x, event.y)

    def __move_to(self, event):
        """Drag (move) canvas to the new position"""

        self.canvas.scan_dragto(event.x, event.y, gain=1)
        self.redraw()  # redraw the image

    def __wheel(self, event):
        """Zoom with mouse __wheel"""

        x = self.canvas.canvasx(event.x)
        y = self.canvas.canvasy(event.y)
        scale = 1.0
        if event.num == 5 or event.delta == -globals.SCROLL_DELTA:  # scroll down
            self.canvas.imscale /= self.delta
            scale /= self.delta
        if event.num == 4 or event.delta == globals.SCROLL_DELTA:  # scroll up
            self.canvas.imscale *= self.delta
            scale *= self.delta
        # rescale all canvas objects
        self.canvas.scale("all", x, y, scale, scale)
        self.redraw()

    def redraw(self, *args):
        self.canvas.show()


class MegaButton:
    """Window with scrollbar and parameter input box"""

    def __init__(self, varname, root):
        self.scrollbar = tk.Scale(
            root,
            from_=-100,
            to=100,
            tickinterval=1,
            borderwidth=5,
            orient=tk.VERTICAL,
            bg=root.interface_color,
            font=root.interface_font,
        )

        self.scrollbar.configure(command=root._read_params_from_scrollbar)

        self.input_param = tk.Text(
            root,
            bg=root.interface_color,
            width=4,
            height=3,
            padx=10,
            pady=10,
            font=root.interface_font,
        )

        self.varname_label = tk.Label(
            text=varname,
            width=2,
            height=5,
            padx=10,
            pady=13,
            bg=root.interface_color,
            font=root.interface_font,
        )

        self.del_button = tk.Button(
            root,
            height=1,
            width=1,
            text="X",
            bg=root.interface_color,
            command=lambda: root._del_megabutton(varname),
            font=root.interface_font,
        )

        self.push_param_button = tk.Button(
            root,
            height=1,
            width=3,
            text="Push",
            bg=root.interface_color,
            command=lambda: root._read_params_from_keyboard(var=varname),
            font=root.interface_font,
        )

    def place(self, x_pos, y_pos):
        self.scrollbar.place(x=x_pos, y=y_pos)

        self.input_param.place(x=x_pos, y=y_pos)

        self.varname_label.place(x=x_pos + globals.SCROLLBAR_SZ[0], y=y_pos)
        self.del_button.place(x=x_pos + globals.SCROLLBAR_SZ[0], y=y_pos)
        self.push_param_button.place(x=x_pos, y=y_pos + 75)

    def destroy(self):
        self.scrollbar.destroy()
        self.del_button.destroy()
        self.input_param.destroy()
        self.push_param_button.destroy()
        self.varname_label.destroy()


class FigureLabel:
    """Label with function name and delete button"""

    def __init__(self, label, root):
        self.figure_label = tk.Label(
            text=label,
            width=20,
            height=2,
            padx=10,
            pady=10,
            bg=root.interface_color,
            font=root.interface_font,
        )
        self.del_button = tk.Button(
            root,
            height=1,
            width=1,
            text="X",
            command=lambda: root._del_figure_label(label),
            bg=root.interface_color,
            font=root.interface_font,
        )

    def place(self, x_pos, y_pos):
        self.figure_label.place(x=x_pos, y=y_pos)
        self.del_button.place(x=x_pos, y=y_pos)

    def destroy(self):
        self.figure_label.destroy()
        self.del_button.destroy()


class Window(tk.Tk):
    def __show_error(self, text):
        """Brings up an error window"""
        error_window = tk.Tk()
        error_window.geometry("300x100")
        error_window.title(text)
        button = tk.Button(
            error_window,
            width=20,
            height=2,
            text="O K A Y",
            command=lambda: error_window.destroy(),
            font=self.interface_font,
        )
        button.place(x=40, y=20)

    def __create_req_button(self, varname):
        """Creates a parameter request"""
        if varname in self.req_buttons:
            return

        def __bind():
            self.req_buttons.pop(varname)
            self.__create_megabutton(varname)
            req_button.destroy()
            self.__order_req_buttons()

        req_button = tk.Button(
            self,
            height=2,
            width=20,
            text=f"Create parameter {varname} ",
            command=lambda: __bind(),
            bg=self.interface_color,
            font=self.interface_font,
        )
        req_button.place(x=globals.BUTTON_SZ[1] * len(self.req_buttons), y=0)
        self.req_buttons[varname] = (time(), req_button)

    def __create_megabutton(self, varname):
        """Creates megabutton"""
        megabutton = MegaButton(varname, self)
        megabutton.place(
            0, globals.SCROLLBAR_SZ[0] * len(self.megabuttons) + globals.CANV_Y[0]
        )
        self.megabuttons[varname] = (time(), megabutton)

    def __create_figure_label(self, label):
        """Creates figure label"""
        figure_label = FigureLabel(label, self)
        self.figure_labels[label] = (time(), figure_label)
        self.__order_figures_labels()

    def __order_req_buttons(self):
        """Orders request buttons"""
        c = 0
        for t, req_button in self.req_buttons.values():
            req_button.place(x=globals.BUTTON_SZ[1] * c, y=0)
            c += 1

    def __order_figures_labels(self):
        """Orders figures labels"""
        c = 0
        for t, figure_label in self.figure_labels.values():
            figure_label.place(
                x_pos=globals.CANV_X[1],
                y_pos=globals.CANV_Y[0] + globals.DEL_BUTTON_SZ[0] * c,
            )
            c += 1

    def __order_megabuttons(self):
        """Orders megabuttons"""
        c = 0
        for t, megabutton in self.megabuttons.values():
            megabutton.place(0, globals.SCROLLBAR_SZ[0] * c + globals.CANV_Y[0])
            c += 1

    def __delete_unnecessary_req_buttons(self):
        """Deletes request buttons pending for non-existing parameter"""
        actual_params = self.__get_actual_params()
        todestroy = set()
        for req_param in self.req_buttons:
            if req_param not in actual_params:
                todestroy |= {req_param}
        for param in todestroy:
            self.req_buttons[param][1].destroy()
            self.req_buttons.pop(param)
        self.__order_req_buttons()

    def _del_figure_label(self, label):
        """Deletes figure from canvas and it's label"""
        self.app.canvas.figures.pop(label)
        self.figure_labels[label][1].destroy()

        self.figure_labels.pop(label)

        self.__order_figures_labels()
        self.__delete_unnecessary_req_buttons()

        self.app.redraw()

    def _del_megabutton(self, varname):
        """Deletes megabutton"""
        self.megabuttons[varname][1].destroy()
        self.megabuttons.pop(varname)
        if varname in globals.global_kwargs:
            globals.global_kwargs.pop(varname)
        if varname in self.__get_actual_params():
            self.__create_req_button(varname)
        self.update()
        self.app.redraw()
        self.__order_megabuttons()
        pass

    def _read_params_from_scrollbar(self, *args):
        """Reads parameters from all scrollbars"""
        for var in self.megabuttons:
            bar = self.megabuttons[var][1].scrollbar
            globals.global_kwargs[var] = bar.get()
        self.app.redraw()

    def _read_params_from_keyboard(self, var, *args):
        """Reads parameters from all scrollbars"""
        input_param = self.megabuttons[var][1].input_param
        param = input_param.get("1.0", "end-1c")
        input_param.delete("1.0", tk.END)

        param = param.strip()
        param = param.rstrip()
        try:
            param = float(param)
            globals.global_kwargs[var] = param
        except:
            self.__show_error("PARAMS MUST BE DECIMALS")
        self.app.redraw()

    def __read_func_name(self):
        """Reads function as a string, adds function to canvas and adds it's label to the window"""
        raw_str_func = self.text_input.get("1.0", "end-1c")
        raw_str_func = (raw_str_func.rstrip()).lstrip()
        raw_str_func = raw_str_func.replace(" ", "")
        str_func, varnames = process(raw_str_func)
        if raw_str_func in self.figure_labels:
            return

        def func(x, kwargs):
            return eval(str_func)

        if not evaltest_function(func, varnames):
            self.__show_error("Wrong function")
            return

        for varname in varnames:
            if varname not in globals.global_kwargs and varname not in self.req_buttons:
                self.__create_req_button(varname)

        figure = FuncGraph(func, label=raw_str_func)
        self.app.canvas.add_figure(figure)
        self.__create_figure_label(figure.label)
        self.app.redraw()
        self.text_input.delete("1.0", tk.END)

    def __get_actual_params(self):
        """Return existing parameters"""
        actual_params = set()
        for f in self.app.canvas.figures:
            varnames = process(f)[1]
            actual_params |= varnames
        return actual_params

    def __clear(self):
        """Deletes all objects from the window"""

        for t, figure_label in self.figure_labels.values():
            figure_label.destroy()
        for t, req_button in self.req_buttons.values():
            req_button.destroy()
        for t, megabutton in self.megabuttons.values():
            megabutton.destroy()

        globals.global_kwargs = {}

        self.figure_labels = {}
        self.req_buttons = {}
        self.megabuttons = {}
        self.app.canvas.figures = {}

        self.app.redraw()

    def __init__(self):
        """Initializes the main Frame"""

        super().__init__()

        self.interface_font = ("Comic Sans MS", 12, "bold")
        self.interface_color = "RosyBrown1"
        self.color = "pink2"

        self.button_plot = tk.Button(
            self,
            height=2,
            width=20,
            text="Plot it",
            command=lambda: self.__read_func_name(),
            bg=self.interface_color,
            font=self.interface_font,
        )

        self.button_clear = tk.Button(
            self,
            height=2,
            width=20,
            text="Clear all",
            command=lambda: self.__clear(),
            bg=self.interface_color,
            font=self.interface_font,
        )

        self.label_input = tk.Label(
            text="Enter your function\n e.g. -x + 2 * sin(x / 2)",
            width=25,
            height=1,
            padx=10,
            pady=10,
            bg=self.interface_color,
            font=self.interface_font,
        )
        self.text_input = tk.Text(
            self,
            bg=self.interface_color,
            width=25,
            height=3,
            padx=10,
            pady=10,
            font=self.interface_font,
        )

        self.app = UI(self, width=globals.CANV_SZ[1], height=globals.CANV_SZ[0])

        self.configure(background=self.color)
        self.geometry("800x600")
        self.title(" GraphPlotter3000 ")

        self.figure_labels = OrderedDict()
        self.req_buttons = OrderedDict()
        self.megabuttons = OrderedDict()

        self.app.canvas.place(x=globals.CANV_X[0], y=globals.CANV_Y[0])
        self.label_input.place(x=globals.CANV_X[0], y=globals.CANV_Y[1])
        self.text_input.place(x=globals.CANV_X[0], y=globals.CANV_Y[1] + 40)
        self.button_plot.place(
            x=-globals.BUTTON_SZ[1] + globals.CANV_X[1], y=globals.CANV_Y[1]
        )
        self.button_clear.place(
            x=-globals.BUTTON_SZ[1] + globals.CANV_X[1], y=globals.CANV_Y[1] + 65
        )
