"""
Select minimum and maximum complexity analysis:

By grouping the elements in groups of 2,
then comparing the minimum with the smaller number
then comparing the maximum with the larger number

We only need to do 3 comparisons for every 2 numbers.
Which is better than finding, max and then finding min separately
Therefore:

Time complexity:
    O(1.5n)

Space complexity:
    O(1)

"""


def select_min_max(arr):
    if len(arr) == 0:
        raise ValueError
    arr_min = arr[0]
    arr_max = arr[0]

    for i in range(len(arr)//2):
        if arr[2*i] < arr[2*i+1]:
            if arr[2*i] < arr_min:
                arr_min = arr[2*i]
            if arr[2*i+1] > arr_max:
                arr_max = arr[2*i+1]
        else:
            if arr[2*i+1] < arr_min:
                arr_min = arr[2*i+1]
            if arr[2*i] > arr_max:
                arr_max = arr[2*i]
    
    if len(arr) % 2 == 1: # if odd, then check the last element
        if arr[-1] < arr_min:
            arr_min = arr[-1]
        if arr[-1] > arr_max:
            arr_max = arr[-1]

    return arr_min, arr_max