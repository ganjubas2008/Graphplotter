import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import messagebox
import pytest

import sys
sys.path.append("src")
from user_interface import *

@pytest.fixture
def root():
    root = tk.Tk()
    root.interface_color = 'white'
    root.interface_font = ('Arial', 12)
    root._del_figure_label = lambda label: None
    return root

def test_scrollbar_visible():
    root = tk.Tk()
    txt = scrolledtext.ScrolledText(root)
    txt.grid(column=0, row=0, sticky='nsew')
    assert txt.yview() == (0.0, 0.058823529411764705)
    root.update()

    # AutoScrollbar should not be visible if scrollbar is not needed
    vsb = AutoScrollbar(root, orient='vertical', command=txt.yview)
    vsb.grid(column=1, row=0, sticky='ns')
    assert vsb.grid_info()['columnspan'] == 1
    root.destroy()


def test_scrollbar_hidden():
    root = tk.Tk()
    txt = scrolledtext.ScrolledText(root)
    txt.insert(tk.END, "Test\n" * 100)
    txt.grid(column=0, row=0, sticky='nsew')
    assert txt.yview() == (0.0, 0.0005824111822947001)
    root.update()

    # AutoScrollbar should be visible if scrollbar is needed
    vsb = AutoScrollbar(root, orient='vertical', command=txt.yview)
    vsb.grid(column=1, row=0, sticky='ns')
    assert vsb.grid_info() != {}
    root.destroy()

def test_figure_label_place(root):
    figure_label = FigureLabel('Test', root)
    figure_label.place(10, 20)

def test_figure_label_destroy(root):
    figure_label = FigureLabel('Test', root)
    figure_label.place(10, 20)
    figure_label.destroy()
    assert figure_label.figure_label.winfo_exists() == False
    assert figure_label.del_button.winfo_exists() == False