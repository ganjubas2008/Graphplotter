import pytest
import sys
sys.path.append("src")
from figure_types import *

def test_build_zero_size():
    func_graph = FuncGraph(lambda x: x ** 2, 'x^2')
    func_graph.build(-5, 5, 0, 25, 1)
    assert len(func_graph.vecs) == 0

def test_str():
    func_graph = FuncGraph(lambda x: x ** 2, '-1^-1')
    func_graph.build(-5, 5, 0, 25, 10)
    assert not str(func_graph)