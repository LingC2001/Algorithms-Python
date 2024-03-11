import sys
sys.path.append("./")
from binary_search import binary_search
import pytest

@pytest.fixture
def arr():
    return [-15, 1, 3, 4, 5, 6, 11, 14, 16, 19, 21, 33, 35]

def test_target_in_arr(arr):
    assert binary_search(arr, 6) == arr.index(6)

def test_target_not_in_arr(arr):
    assert binary_search(arr, 7) == -1

def test_target_at_front(arr):
    assert binary_search(arr, arr[0]) == 0

def test_target_at_back(arr):
    assert binary_search(arr, arr[-1]) == len(arr)-1

def test_negative_numbers(arr):
    assert binary_search(arr, -15) == arr.index(-15)

def test_negative_numbers_not_in(arr):
    assert binary_search(arr, -16) == -1

def test_target_smaller_than_all_elements(arr):
    assert binary_search(arr, -20) == -1

def test_target_larger_than_all_elements(arr):
    assert binary_search(arr, 123) == -1

def test_input_error(arr):
    with pytest.raises(TypeError):
        binary_search(arr, "6")