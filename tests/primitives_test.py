import pytest
import sys
sys.path.append("src")
from primitives import *

def test_addition():
    v1 = Vec2d(1, 2)
    v2 = Vec2d(3, 4)
    assert v1 + v2 == Vec2d(4, 6)

def test_subtraction():
    v1 = Vec2d(1, 2)
    v2 = Vec2d(3, 4)
    assert v2 - v1 == Vec2d(2, 2)

def test_multiplication():
    v1 = Vec2d(1, 2)
    assert v1 * 3 == Vec2d(3, 6)

def test_division():
    v1 = Vec2d(1, 2)
    assert v1 / 2 == Vec2d(0.5, 1)

def test_mirroring():
    v1 = Vec2d(1, 2)
    assert v1.mirror() == Vec2d(1, -2)

def test_string_representation():
    v1 = Vec2d(1.2345678, 2.3456789)
    assert str(v1) == "[1.23, 2.35]"
