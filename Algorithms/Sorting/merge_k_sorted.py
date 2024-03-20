def merge_k_sorted(arrs):
    """
    basically just merge sort but with arrays
    """
    if len(arrs) == 0:
        return []
    elif len(arrs) == 1:
        return arrs[0]
    else:
        mid = len(arrs)//2
        left = merge_k_sorted(arrs[:mid])
        right = merge_k_sorted(arrs[mid:])
        return merge(left, right)

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