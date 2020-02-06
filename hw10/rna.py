from collections import defaultdict, OrderedDict

from heapq import heappush, heappop
 
allowed = set(['AU','UA','CG','GC','GU','UG'])

def best(x):
    
    def _best(i,j):
        if (i,j) in opt:
            return opt[i,j]
        curr = -1
        for k in range(i, j):
            if _best(i,k) + _best(k+1,j) > curr:
                curr = _best(i,k) + _best(k+1,j)
                back[i, j] = k
        
        
        if x[i] + x[j] in allowed:
            if _best(i+1, j-1) + 1 > curr:
                curr = _best(i+1, j-1) + 1
                back[i, j] = -1
        opt[i, j] = curr
        return curr
        
        
    def solution(i, j):
        if i == j:
            return "."
        if i > j:
            return ""
        
        k = back[i, j]
        if k == -1:
            return "(%s)" % solution(i+1, j-1)
        else:
            return solution(i, k) + solution(k+1, j)
        
    opt = defaultdict(lambda:0)
    back = {}
    n = len(x)
    for i in range(n):
        opt[i, i] = 0
        opt[i, i-1] = 0
        
        
    return _best(0, n-1), solution(0, n-1)
    
#print(best('CGAGGUGGCACUGACCAAACACCACCGAAAC'))


def total(x):

    def _total(i,j):
        if (i,j) in opt:
            return opt[i,j]
        curr = 0
        for k in range(i, j):
            if x[k] + x[j] in allowed:
                curr += _total(i, k-1) * _total(k+1,j-1)
        
        curr += _total(i, j-1)
        opt[i, j] = curr
        return curr
        
        
    opt = defaultdict(lambda:0)
    n = len(x)
    for i in range(n):
        opt[i, i] = 1
        opt[i, i-1] = 1
        
        
    return _total(0, n-1)
    
    
#print(total("ACAGU"))
    
def kbest(x, k):
    def _kbest(i, j, dep=0):
        def trypush_b(s, p, q):
            if p < len(topk[i,s]) and q < len(topk[s+1, j]) and (s,p,q) not in visited:
                heappush(h, (-(topk[i,s][p][0] + topk[s+1,j][q][0]), (s,p,q)))
                visited.add((s,p,q))
                
        def trypush_u(p):
            if p < len(topk[i+1, j-1]):
                heappush(h, (-(topk[i+1, j-1][p][0] + 1), (p,)))
            
        if (i,j) in topk:
            return topk[i,j]
#        if i == j:
#            topk[i,j] = [(0, '.')]
#            return
#        elif j == i-1:
#            topk[i,i-1] = [(0,'')]
#            return
            
        h = []
        visited = set()
        for s in range(i,j):
            _kbest(i, s, dep+1)
            _kbest(s+1, j, dep+1)
            trypush_b(s, 0, 0)
        if x[i] + x[j] in allowed:
            _kbest(i+1, j-1, dep+1)
            trypush_u(0)
        
        
        used = set()
        while len(topk[i,j]) < k:
            if h == []:
                break
            score, indicies = heappop(h)
            try:
                s,p,q = indicies
                foldStr = "%s%s" % (topk[i,s][p][1], topk[s+1,j][q][1])
                if (-score, foldStr) not in used:
                    topk[i,j].append((-score, foldStr))
                    used.add((-score, foldStr))
                trypush_b(s,p+1, q)
                trypush_b(s, p, q+1)
            except:
                p = indicies[0]
                foldStr = "(%s)" % topk[i+1, j-1][p][1]
                if (-score, foldStr) not in used:
                    topk[i, j].append((-score, foldStr))
                    used.add((-score, foldStr))
                trypush_u(p+1)
                    
                
    topk = defaultdict(list)
    n = len(x)
    for i in range(n):
        topk[i, i] = [(0, '.')]
        topk[i, i-1] = [(0, '')]
    _kbest(0, n-1)
    

    fin = OrderedDict()
    k_v = 0
    for j in reversed(range(n)):
        for v in topk[0,j]:
            if k_v < k:
                if v not in fin:
                    fin[v] = v
                    k_v += 1


    out = list(fin.keys())

    
    return out
            
#print(kbest("UCAGAGGCAUCAAACCU", 300))

