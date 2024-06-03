

def binary_search_interval(nums, target):
    """
    Given a sorted array of numbers,
    Gets the range of the values equal to target in the form (start_inclusive, end_exclusive)
    If target does not exist in the nums array, then start and end index will be the same
    """
    start_inclusive = binary_search_start(nums, target)
    end_exclusive = binary_search_end(nums, target)
    return start_inclusive, end_exclusive




def binary_search_start(nums, target):
    """
    Algorithm correctness analysis:
    
    When mid != target, left and right pointers will converge towards the target.
    When mid == target, we want to check the left side for first position of the target.

    Case 1: target = 3
        ['L=1', 1, 1, 1, 1, 1, 1, 'M=3', 3, 3, 3, 3, 5, 5, 5, 'R=5']
        ['L=1', 1, 1, 'M=1', 1, 1, 'R=1', 3, 3, 3, 3, 3, 5, 5, 5, 5]
        [1, 1, 1, 1, 'L=1', 'M=1', 'R=1', 3, 3, 3, 3, 3, 5, 5, 5, 5]
        [1, 1, 1, 1, 1, 1, 'M=R=L=1', 3, 3, 3, 3, 3, 5, 5, 5, 5]
            - left mid and right converge to the index before first pos
        [1, 1, 1, 1, 1, 1, 'M=R=1', 'L=3', 3, 3, 3, 3, 5, 5, 5, 5]
            - left is pushed to the correct position at the end
        
    Case 2: target = 3
        ['L=1', 1, 1, 1, 1, 1, 3, 'M=3', 3, 3, 3, 3, 5, 5, 5, 'R=5']
        ['L=1', 1, 1, 'M=1', 1, 1, 'R=3', 3, 3, 3, 3, 3, 5, 5, 5, 5]
        [1, 1, 1, 1, 'L=1', 'M=1', 'R=3', 3, 3, 3, 3, 3, 5, 5, 5, 5]
        [1, 1, 1, 1, 1, 1, 'M=R=L=3', 3, 3, 3, 3, 3, 5, 5, 5, 5]
            - left mid and right converge to the correct position
        [1, 1, 1, 1, 1, 'R=1', 'M=L=3', 3, 3, 3, 3, 3, 5, 5, 5, 5]
            - right is pushed to before, and left remains at the correct positions
    
    Case 3: target = 4 (does not exist)
        ['L=1', 1, 1, 1, 1, 1, 3, 'M=3', 3, 3, 3, 3, 5, 5, 5, 'R=5']
        [1, 1, 1, 1, 1, 1, 3, 3, 'L=3', 3, 3, 'M=3', 5, 5, 5, 'R=5']
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 'L=5', 'M=5', 5, 'R=5']
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 'M=R=L=5', 5, 5, 5]
        [1, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 'R=3', 'M=L=5', 5, 5, 5]
            - left pointer is at the insert position. 
                a.k.a 4 should be inserted at left pointer index

    Basically, since the algorithm terminates when l > r, this happens at the last iteration
    when l = r + 1.
    l is always ends to the right of the boundary
    r is always ends to the left of the boundary

    thus returning left gives us the index of first occurrence, or the insert position if 
    target doesn't exist.
    """

    l = 0
    r = len(nums)-1

    while l <= r:
        mid = l + (r-l)//2 # avoid integer overflow when l and r are large positive integers
        # visualise(nums, l, r, mid)
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else: # if nums[mid] == target
            r = mid - 1 # check left side
    # visualise(nums, l, r, mid)
    print(f"start_inclusive: {l}")
    return l


def binary_search_end(nums, target):
    """
    When mid != target, left and right pointers will converge towards the target.
    When mid == target, we want to check the right side for the last position of the target.

    Basically, since the algorithm terminates when l > r, this happens at the last iteration
    when l = r + 1.
    l is always ends to the right of the boundary
    r is always ends to the left of the boundary

    thus returning right gives us the inclusive index of last position
    returning left gives us the exclusive index and the insert index if it doesn't exist
    """
    l = 0
    r = len(nums)-1

    while l <= r:
        mid = l + (r-l)//2
        # visualise(nums, l, r, mid)
        if target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
        else: # if nums[mid] == target
            l = mid + 1 # check right side
        # visualise(nums, l, r, mid)
    print(f"end_exclusive: {l}")
    return l


def visualise(nums, l, r, mid):
    nums_copy = [x for x in nums]
    nums_copy[l] = f'L={nums_copy[l]}'
    nums_copy[r] = f'R={nums_copy[r]}'
    nums_copy[mid] = f'M={nums_copy[mid]}'
    print(nums_copy)
