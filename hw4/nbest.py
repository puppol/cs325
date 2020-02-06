a, b = [4, 1, 5, 3], [2, 6, 3, 4]


def nbesta(a,b):
    combined = [(x,y, x+y) for x in a for y in b]
    combined.sort(key=lambda x:(x[2],x[1]))
    return [(t[0],t[1]) for t in combined[:len(a)]]


import random

def qselect(i, a):
    if a == []:
        return []
    idx=random.randint(0,len(a)-1)
    pivot = a[idx]

    a[0],a[idx]=a[idx],a[0]

    left = [x for x in a if x[2] < pivot[2] or (x[2] == pivot[2] and x[1] < pivot[1])]
    if len(left) == i-1:
        return pivot
    if len(left) < i - 1:
        right = [x for x in a[1:] if x[2] > pivot[2] or (x[2] == pivot[2] and x[1] > pivot[1])]
        return qselect(i-len(left)-1,right)
    else:
        # a = left
        return qselect(i,left)



def nbestb(a,b):
    combined = [(x,y, x+y) for x in a for y in b]
    topn = [qselect(i+1, combined) for i in range(len(a))]
    
    return [(t[0],t[1]) for t in topn]
    
    

import heapq
def nbestc(a,b):
    heapq.heapify(a)
    heapq.heapify(b)
    len_a = len(a)
    candidateHeap = [(a[0] + b[0], heapq.popheap(b), heapq.popheap(a))] 

    while len(candidateHeap) < len_a * 2:
        left = heapq.heappop(a)
        right = heapq.heappop(b)
        heapq.pushheap(candidateHeap, (left+right,right,left))
	

    
    return [heapq.heappop(candidateHeap) for _ in range(len_a)]

