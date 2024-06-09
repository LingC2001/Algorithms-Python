"""
Radix sort complexity analysis

Radix sort simply applies counting sort k-times, once for each digit of the 
input. The range of numbers for each counting sort is just b, where b is the base
of the digits. E.g. counting sort in base 10, would have a range of 10,
aka. u = b = 10

Time complexity
    Each counting sort takes O(n + b) time.
    Therefore radix sort for k-digit integers would be:
    O(k(n+b))

Space complexity:
    Just the space complexity of each counting sort
    O(n+b)

    
Notice that number of digits "k" and the base "b" are inversely porpotionate.
larger base = less digits and smaller base = more digits.
More specifically: k = w/log(b)
So, time: O(w/log(b) * (n+b))
We want as large of a base as possible to minimize k and not slow down individual 
counting sort. Therefore we choose b = n, so that counting sort is still O(n)
Therefore time: O(w/log(n) * n), space: O(n)
Hence, radix sort is still O(n) as long as w/log(n) = O(1), aka w = O(log(n)). 
aka. when radix sort has integers of at most c*log(n) bits.

This means the maximum size of the input can be 2^w = 2^(clog(n)) = n^c, which we 
can see if better than counting sort where input could only be O(n)
"""


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