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
    counter = [0] * (max_range-min_range + 1)

    # count occurence of each number
    for num in nums:
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
    for i in range(1, len(counter)):
        temp = counter[i]
        counter[i] = prev + counter[i-1]
        prev = temp

    # sort array
    res = [0] * len(nums)
    for num in nums:
        res[counter[num+shift]] = num
        counter[num+shift] += 1
    return res

