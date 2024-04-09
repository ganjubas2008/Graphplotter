import pytest
import sys
sys.path.append("src")
from util import *

def test_process():
    input_str = "x^2 + y^2"
    expected_output_str = "x**2 + globals.global_kwargs['y']**2"
    expected_varnames = {"y"}

    # Test the function output
    output_str, varnames = process(input_str)
    assert output_str == expected_output_str
    assert varnames == expected_varnames

    # Test that the output string can be used to evaluate a function
    def f(x, kwargs):
        return eval("input_str")

    assert evaltest_function(f, varnames)

def test_cute_round():
    # Test integer values
    assert cute_round(1, 0) == 1

    # Test decimal values
    assert cute_round(0.1234, 2) == 0.12
    assert cute_round(0.1234, 3) == 0.123

    # Test values with fractional part > 0.5
    assert cute_round(1.6, 0) == 2
    assert cute_round(0.6, 0) == 1

def test_cute_float():
    # Test values with delta >= 1000
    assert cute_float(123456.789, 1000) == "123456.8"
    assert cute_float(1234.56789, 100) == "1234.6"

    # Test values with 1 <= delta < 1000
    assert cute_float(123.456789, 1) == "123.46"
    assert cute_float(12.3456789, 0.1) == "12.35"
    assert cute_float(1.23456789, 0.01) == "12.35e-1"

    # Test values with delta < 1
    assert cute_float(0.123456789, 0.001) == "12.35e-2"
    assert cute_float(0.0123456789, 0.0001) == "12.35e-3"
    assert cute_float(0.00123456789, 0.00001) == "123.46e-5"
