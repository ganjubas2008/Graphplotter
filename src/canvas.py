import random
import tkinter as tk
from tkinter import ttk
from math import *
from figure_types import *
from util import *
import globals


class xCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.imscale = 1.0  # scale for the canvas image

        self.garbage = []  # Stores objects on canvas to be desructed

        # Container to determine origin position
        self.container = self.create_rectangle(0, 0, 0, 0, width=0)

        self.figures = {}

        self.accuracy = globals.CANV_ACCURACY  # Number of points in graphs of functions

    def __clear(self):
        for i in self.garbage:
            self.delete(i)
        self.garbage = []

    def __cart(self, vec):
        """Get cartesian coodrinates of point given in canvas coordinate system"""

        k = 1 / self.imscale
        zero = Vec2d(*self.bbox(self.container)[:2])
        return ((vec - zero) * k).mirror()

    def __canv(self, vec):
        """Get coodrinates in canvas coordinate system of point given in cartesian coordinate system"""

        k = 1 / self.imscale
        zero = Vec2d(*self.bbox(self.container)[:2])
        return vec.mirror() / k + zero

    def add_figure(self, g):
        if g.color == "":
            g.color = globals.COLORS[random.randint(0, len(globals.COLORS) - 1)]
        self.figures[g.label] = g

    def add_axes(self):
        nw = Vec2d(self.canvasx(0), self.canvasy(0))  # get visible area
        se = Vec2d(self.canvasx(self.winfo_width()), self.canvasy(self.winfo_height()))

        zero = Vec2d(*self.bbox(self.container)[:2])

        cart_nw = self.__cart(nw)
        cart_se = self.__cart(se)
        minx = cart_nw.x
        miny = cart_se.y
        maxx = cart_se.x
        maxy = cart_nw.y

        delta = maxx - minx
        mark_count = 10
        stepr = 2 ** int(log(delta / mark_count, 2)) * 2.5

        self.garbage.append(self.create_line(nw.x, zero.y, se.x, zero.y))
        x = minx // stepr * stepr
        while x <= maxx:
            pos = self.__canv(Vec2d(x, 0))
            if x == 0:
                self.garbage.append(
                    self.create_text(
                        pos.x + 15,
                        pos.y + 15,
                        text="0",
                        fill="black",
                        font=("Helvectica", "8"),
                    )
                )
            else:
                self.garbage.append(
                    self.create_line(pos.x, pos.y - 2, pos.x, pos.y + 2)
                )
                self.garbage.append(
                    self.create_text(
                        pos.x,
                        pos.y + 20,
                        text=cute_float(x, delta),
                        fill="black",
                        font=("Helvectica", "8"),
                    )
                )
            x += stepr

        self.garbage.append(self.create_line(zero.x, nw.y, zero.x, se.y))
        y = miny // stepr * stepr
        while y <= maxy:
            if y != 0:
                pos = self.__canv(Vec2d(0, y))

                self.garbage.append(
                    self.create_line(pos.x - 2, pos.y, pos.x + 2, pos.y)
                )
                self.garbage.append(
                    self.create_text(
                        pos.x + 20,
                        pos.y,
                        text=cute_float(y, delta),
                        fill="black",
                        font=("Helvectica", "8"),
                    )
                )
            y += stepr

    def show(self, event=None):
        """Draw all visible objects on canvas"""

        self.__clear()

        nw = Vec2d(self.canvasx(0), self.canvasy(0))  # get visible area
        se = Vec2d(self.canvasx(self.winfo_width()), self.canvasy(self.winfo_height()))
        zero = Vec2d(*self.bbox(self.container)[:2])

        cart_nw = self.__cart(nw)
        cart_se = self.__cart(se)

        minx = cart_nw.x
        miny = cart_se.y
        maxx = cart_se.x
        maxy = cart_nw.y

        for g in self.figures.values():

            if type(g) == FuncGraph:
                # todo: fix miny, maxy
                g.build(minx, maxx, miny, maxy, self.accuracy)
                for i in range(1, len(g.vecs)):

                    prev = self.__canv(g.vecs[i - 1])
                    cur = self.__canv(g.vecs[i])
                    self.garbage.append(
                        self.create_line(
                            prev.x,
                            prev.y,
                            cur.x,
                            cur.y,
                            width=2,
                            fill=g.color,
                        )
                    )

            if type(g) == PointGraph:
                d = globals.INF  # Point radius
                for i in range(1, len(g.vecs)):

                    prev = self.__canv(g.vecs[i - 1])
                    cur = self.__canv(g.vecs[i])

                    if nw.y < cur.y and cur.y < se.y:
                        deltav = prev - cur
                        d = min(abs(deltav.x), abs(deltav.y), d)
                d = min(d / 3, 5)
                for cart_v in g.vecs:
                    v = self.__canv(cart_v)
                    if nw.y < v.y and v.y < se.y:
                        self.garbage.append(
                            self.create_oval(
                                v.x - d,
                                v.y - d,
                                v.x + d,
                                v.y + d,
                                width=2,
                                fill=g.color,
                            )
                        )

        self.add_axes()

    def draw_legend():
        pass

    def set_label(s):
        pass
