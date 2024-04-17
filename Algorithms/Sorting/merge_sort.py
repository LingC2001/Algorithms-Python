"""
Merge sort complexity analysis:

Time complexity:
    The input is halved at every level until there is only 1 element left.
    Therefore the depth is O(log2(n)).
    At each level, n-elements are merged therefore O(n)
    So in total, O(nlog(n))

Space complexity:
    Firstly, we can see that in each recursive call, we pass down half of the array.
    Therefore, the call stack uses at most O(3n)
        - which can be optimized to O(1) if we used indicies instead of list splicing

    The merge routine creates a new merged array every merge function call, 
    which at most O(n), however this memory is freed as soon as the merge finishes.

    So total space complexity: O(n)

"""


def merge_sort(nums):
    if len(nums) <= 1: # base case only 1 element left
        return nums # already sorted
    else: # more than 1 element left in sub-array, keep splitting
        mid = len(nums)//2
        left = merge_sort(nums[:mid]) # returns left half sorted
        right = merge_sort(nums[mid:]) # returns right half sorted
        return merge(left, right) # merge 2 halves
    
def merge(left, right):
    l = 0
    r = 0
    merged = []
    while l <= len(left)-1 or r <= len(right)-1:
        if l >= len(left): # left arr empty
            merged.append(right[r])
            r += 1
        elif r >= len(right): # right arr empty
            merged.append(left[l])
            l += 1
        else:
            if left[l] <= right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
    return merged