"""
Binary Search complexity analysis:

Time complexity:
    Since the input size halves for every iteration, performing constant time operations,
    we have the recurrence relation:
                    T(n) = T(n/2) + a
                    T(1) = b
    Solving this recurrence relation through induction gives us:
                    T(n) = alog2(n) + b
    So therefore O(log(n))

Space Complexity:
    The auxiliary complexity is O(1), because only variables like "l", "r", "mid"
    are used.
    
"""



def binary_search(nums, target):
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = (l+r)//2
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else:
            return mid
    return -1

