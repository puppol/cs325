from heapq import heappush, heappop, heapify
def nbest(ABs):    # no need to pass in k or n
    k = len(ABs)
    n = len(ABs[0][0])
    def trypush(i, p, q):  # push pair (A_i,p, B_i,q) if possible
        A, B = ABs[i] # A_i, B_i
        if p < n and q < n and (i,p,q) not in used:
            heappush(h, (A[p]+B[q], i, p, q, (A[p],B[q])))
            used.add((i, p, q))
    h, used = [], set()                 # initialize
    
    
    for i in range(k):
        A, B = ABs[i]
        h.append((A[0]+B[0], i, 0, 0, (A[0],B[0])))
    heapify(h)

    for _ in range(n):
        _, i, p, q, pair = heappop(h)
        yield pair     # return the next pair (in a lazy list)
        trypush(i,p+1,q)
        trypush(i,p,q+1)


print(list(nbest([([1,4],[5,6]),([3,7],[1,5]),([2,4],[3,8])])))
print(list(nbest([([1,6,8,13],[5,8,11,12]),([1,2,3,5],[5,9,11,13]),([3,5,7,10],[4,6,7,11]),([1,4,7,8],[4,9,11,15]),([4,8,10,13],[4,6,10,11]),([4,8,12,15],[5,10,11,13]),([2,3,4,8],[4,7,11,15]),([4,5,10,15],[5,6,7,8])])))
