"""
Counting sort complexity analysis:

    1. Creating a list of range [min:max] and counting occurence of each number
        # O(u) space, O(N) time
    2. Calculate starting index(pos) of each number after sorted
        # O(u) space if new array created, O(1) space if reusing counter array
        # O(u) time, each entry in counter is accumulatively summed
    3. Sort array by placing elements in original array into the correct position in new array
    based off of calculated starting indices
        # O(N) time every num in original list is checked
        # O(N) space, new array of size n created

    Therefore we can see that:
    Time complexity:
        O(n+u)
    Space complexity:
        O(n+u)
    , where u is the maximum value or range of values

    Another way to look at it is look at the width of the integers in binary.
    if w-bits are used to represent a number, then we can say the
    Time and space complexity are: O(n + 2^w), since the maximum value (u) that we can
    represent with w bits is u = 2^w-1

    This means that O(n+u) is only linear O(n) if O(u) is linear, aka if 2^w-1 = n,
    so w = log2(n+1)
        - if there are more bits than this, then counting sort would not be O(n)

"""

import math
def counting_sort(nums):
    """
    Implemented for sorting integers only
    """
    if len(nums) == 0:
        return []
    # find the nums range
    min_range, max_range = math.inf, -math.inf
    for num in nums:
        if not isinstance(num, int):
            raise TypeError
        min_range = min(min_range, num)
        max_range = max(max_range, num)
    shift = 0 - min_range # shifts the minimum number to index 0. min +shift = 0, 
    counter = [0] * (max_range-min_range + 1) #O(u) space

    # count occurence of each number
    for num in nums: # O(N) time
        counter[num+shift] += 1
    
    # calculate starting indexs of each number
    """
    pos = [0] * len(counter)
    for i in range(1, len(counter)):
        pos[i] = counter[i-1] + pos[i-1]
    """
    # calculate starting indexs of each number - optimized space
    prev = counter[0]
    counter[0] = 0
    for i in range(1, len(counter)): #O(u) time
        temp = counter[i]
        counter[i] = prev + counter[i-1]
        prev = temp

    # sort array
    res = [0] * len(nums) # O(n) space
    for num in nums:
        res[counter[num+shift]] = num
        counter[num+shift] += 1
    return res

