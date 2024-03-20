
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

def bucket_sort(arr):
    if not arr:
        return []

    buckets = []
    # for now we will assign number of buckets to be length of array
    # the bucket index to be placed in will be determined by:
    # curr/max * len(buckets)-1
    # this way maximum number will be placed at len(buckets)-1
    # and 0 will be placed at 0*len(buckets)-1 = 0
    n = len(arr)
    for i in range(n):
        buckets.append([])

    # shift all negative numbers to be positive
    shift = 0 - min(arr)
    max_num = max(arr) + shift

    for num in arr:
        idx = int((num+shift)/max_num * (n-1))
        buckets[idx].append(num)

    # we sort the buckets using a stable sorting algorithm (eg insertion sort)
    
    for i in range(n):
        insertion_sort(buckets[i]) # sorting is done in-place


    # combine sorted buckets
    k = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            arr[k] = buckets[i][j]
            k += 1
    
    return None # the original array is modified