
def selection_sort(nums):

    for i in range(len(nums)): # array is sorted for idx [0 -> i-1]
        min_val = nums[i]
        min_idx = i
        for j in range(i, len(nums)):
            if nums[j] < min_val:
                min_val = nums[j]
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i] # array is sorted for idx i
        # i increments by 
    # sorted in place, therefore returning nothing.
    return None
