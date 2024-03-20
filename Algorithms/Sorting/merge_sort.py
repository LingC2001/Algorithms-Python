
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