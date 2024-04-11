import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from fibonacci import fibonacci_top_down, fibonacci_bottom_up
import pytest

def test_bottom_up():
    assert fibonacci_bottom_up(0) == 0
    assert fibonacci_bottom_up(1) == 1
    assert fibonacci_bottom_up(4) == 3
    assert fibonacci_bottom_up(10) == 55
    assert fibonacci_bottom_up(16) == 987
    assert fibonacci_bottom_up(19) == 4181

def test_top_down():
    assert fibonacci_top_down(0) == 0
    assert fibonacci_top_down(1) == 1
    assert fibonacci_top_down(4) == 3
    assert fibonacci_top_down(10) == 55
    assert fibonacci_top_down(16) == 987
    assert fibonacci_top_down(19) == 4181