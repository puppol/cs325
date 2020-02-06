import sys
def find(array, target, k_closest):
    offset = [abs(val - target) for val in array]
    closest, final = ([],[])
    for count in range(k_closest):
        closest.append(offset.index(min(offset)))
        offset[closest[-1]] = sys.maxsize

    closest.sort()
    final = [array[index] for index in closest]
    return final
    

print(find([4,1,3,2,7,4], 6.5, 3))   # returns   [4,7,4]
print(find([5,3,4,1,6,3], 3.5, 2))   # returns   [3,4]
