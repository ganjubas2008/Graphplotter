import pytest
import sys
sys.path.append("src")
from canvas import *

@pytest.fixture
def canvas():
    c = xCanvas(width=300, height=200)
    return c

def test_create_xcanvas():
    # Test creating an instance of xCanvas
    root = tk.Tk()
    canvas = xCanvas(root)
    assert isinstance(canvas, xCanvas)

def test_change_bg_color():
    # Test changing background color of xCanvas
    root = tk.Tk()
    canvas = xCanvas(root)
    canvas.configure(bg="red")
    assert canvas.cget("bg") == "red"

def test_cartesian_conversion(canvas):
    a, b, c, d = 20, 30, 50, 70
    canvas.create_rectangle(20, 30, 50, 70)
    cart_coords = canvas._xCanvas__cart(Vec2d(d / 2, d - a))
    assert cart_coords == Vec2d(d / 2, a - d)
    canvas_coords = canvas._xCanvas__canv(Vec2d(a - d, cart_coords.y))
    assert canvas_coords == Vec2d(a - d, -cart_coords.y)