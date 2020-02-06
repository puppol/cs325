import random
def mergesort(array):
    len_arr = len(array)
    if len_arr <= 1:
        return array
    
    mid_idx = len_arr // 2
    left = array[:mid_idx]
    right = array[mid_idx:]
    left = mergesort(left)
    right = mergesort(right)
    
    
    print(left, right)
    return merge(left, right)
    
    
    
    
def merge(left, right):
    sorted = []
    left_idx, right_idx = (0,0)
    len_left = len(left)
    len_right = len(right)
    while left_idx != len_left and right_idx != len_right:
        if left[left_idx] < right[right_idx]:
            sorted.append(left[left_idx])
            left_idx += 1
        else:
            sorted.append(right[right_idx])
            right_idx += 1
    print(sorted, left, right)
    if left_idx == len_left:
        sorted += right[right_idx:]
    else:
        sorted += left[left_idx:]
    return sorted
