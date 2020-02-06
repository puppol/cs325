def find(array):
    return [(x, y, x+y) for x in array for y in array[x:] if x+y in array[x:]]
    
        
print(find([9,1, 4, 2, 3, 5]))
