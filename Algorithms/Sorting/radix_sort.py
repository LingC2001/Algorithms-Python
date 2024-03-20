
def radix_sort(nums):
    """
    uses base10 counting sort on each digit starting from the end.
    """
    if len(nums) == 0:
        return nums
    
    # deal with negative numbers:
    shift = 0-min(nums) # shift all nums so that negative nums don't exist, then sort

    # get max digit length
    max_len = len(str(max([abs(num) for num in nums]))) # O(3N)
    
    # counting sort each digit
    for i in range(max_len):
        nums = counting_sort(nums, i, shift)
    return nums


def counting_sort(nums, digit, shift):
    """
    Modified counting sort for radix sort
    """
    if len(nums) == 0:
        return []

    counter = [0] * 10

    # count occurence of each number
    for num in nums:
        num_digit = ((num+shift)//(10**digit) ) % 10
        counter[num_digit] += 1
    
    # calculate starting indices of each number
    prev = counter[0]
    counter[0] = 0
    for i in range(1, len(counter)):
        temp = counter[i]
        counter[i] = prev + counter[i-1]
        prev = temp

    # sort array
    res = [0] * len(nums)
    for num in nums:
        num_digit = ( (num+shift)//(10**digit) ) % 10
        res[counter[num_digit]] = num
        counter[num_digit] += 1
    return res