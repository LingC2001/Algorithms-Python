import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from binary_search_interval import binary_search_interval, binary_search_start, binary_search_end
import pytest
import numpy as np 

def assert_correct(nums, target, interval):
    # find first occurrence
    for i in range(len(nums)):
        if nums[i] >= target:
            first = i
            break
    
    # find last occurrence
    for i in range(len(nums)-1, -1, -1):
        if nums[i] <= target:
            last = i+1
            break
    
    assert interval[0] == first
    assert interval[1] == last

    targets = nums[interval[0]:interval[1]]
    assert len(targets) == nums.count(target)
    for num in targets:
        assert num == target



def test_interval():
    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 6
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 3
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [-15, 1, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 19, 21, 33]
    target = 3
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    target = 3
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 4
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 4
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

def test_random():
    nums = sorted(list(np.random.randint(low = 0,high=100,size=1000)))
    target = 1
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = sorted(list(np.random.randint(low = 0,high=100,size=1000)))
    target = 17
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = sorted(list(np.random.randint(low = 0,high=100,size=1000)))
    target = 49
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = sorted(list(np.random.randint(low = 0,high=20,size=1000)))
    target = 17
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)

    nums = sorted(list(np.random.randint(low = 0,high=5,size=1000)))
    target = 4
    print("")
    interval = binary_search_interval(nums, target)
    assert_correct(nums, target, interval)
    



def test_start_index():
    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 6
    print("")
    binary_search_start(nums, target)

    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 3
    print("")
    binary_search_start(nums, target)

    nums = [-15, 1, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 19, 21, 33]
    target = 3
    print("")
    binary_search_start(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_start(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_start(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_start(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 4
    print("")
    binary_search_start(nums, target)

def test_end_index():
    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 6
    print("")
    binary_search_end(nums, target)

    nums = [-15, 1, 3, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 16, 19, 21, 33, 35]
    target = 3
    print("")
    binary_search_end(nums, target)

    nums = [-15, 1, 3, 3, 3, 4, 5, 6, 6, 6, 6, 6, 6, 11, 14, 19, 21, 33]
    target = 3
    print("")
    binary_search_end(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_end(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_end(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 3
    print("")
    binary_search_end(nums, target)

    nums = [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 5, 5, 5, 5]
    target = 4
    print("")
    binary_search_end(nums, target)