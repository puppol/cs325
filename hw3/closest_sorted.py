import bisect


def find(array, target, k_closest):
    mid = bisect.bisect_left(array, target)
    n = len(array)
    
    low, high = (mid, mid)
    closest = 0
    
    while closest != k_closest and low >= 0 and high < n:
        if target - array[low] < array[high] - target:
            low -= 1
        else:
            high += 1
        closest += 1
            
    if low == 0:
        high += k_closest - closest
    if high == n:
        low -= k_closest - closest
    return array[low:high]

print(find([1,2,3,4,4,6,6], 5, 3))
