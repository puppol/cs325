import heapq


def ksmallest(k,a):
    heap = [-1 * x for x in a[:k]]
    heapq.heapify(heap)
    for x in a[k:]:
        x *= -1
        if x > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, x)
            
    heap = [-1 * x for x in heap]
    heap.sort()
    return heap
    


