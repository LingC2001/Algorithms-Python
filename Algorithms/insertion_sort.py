
def insertion_sort(nums):
    # idea: shuffle(insert) the current element to the correct position at each iteration
    # Each iteration sorts 1 element 

    for i in range(len(nums)):
        # arr is sorted for idx 0 -> i-1
        j = i
        while j>0 and nums[j] < nums[j-1]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            j -= 1
        # arr is sorted for idx 0 -> i
        # i = i + 1
    return None # sorted in-place
