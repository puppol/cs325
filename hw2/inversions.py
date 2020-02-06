def mergeSort(arr):
    if len(arr) == 1:
        return arr, 0
    else:
        left = arr[:len(arr) // 2]
        right = arr[len(arr) //2:]
        left, left_inversions = mergeSort(left)
        right, right_inversions = mergeSort(right)
        
        sorted = []
        left_idx, right_idx = (0,0)
        inversions = left_inversions + right_inversions
        
        
        while left_idx < len(left) and right_idx < len(right):
            if left[left_idx] < right[right_idx]:
                sorted.append(left[left_idx])
                left_idx += 1
            else:
                sorted.append(right[right_idx])
                right_idx += 1
                inversions += len(left) - left_idx
        sorted += left[left_idx:]
        sorted += right[right_idx:]
        
        
    return sorted, inversions

def num_inversions(array):
    if array == []:
        return 0
    sorted, inversions = mergeSort(array)
    return inversions

