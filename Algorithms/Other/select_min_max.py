
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