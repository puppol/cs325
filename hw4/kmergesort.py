import heapq

def merge(arrays):
    heap = []
    for array in arrays:
        heap.extend(array)
    heapq.heapify(heap)
    return [heapq.heappop(heap) for _ in range(len(heap))]
    
    
def kmergesort(array, k):
    if len(array) <= 1:
        return array
    return merge([kmergesort(array[i*len(array)//k : (i+1)*len(array)//k ],k) for i in range(k)])
    
    

print(kmergesort([4,1,5,2,6,3,7,0], 3))

