from collections import defaultdict


def _order(n, edges):
    adjlist = defaultdict(list)
    indegree = defaultdict(int)

    for u,v in edges:
        adjlist[u].append(v)
        indegree[v] += 1
            
    queue = [u for u in range(n) if indegree[u] == 0]
            
    head = 0
    while head < len(queue):
        yield queue[head]
        for v in adjlist[queue[head]]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
        head += 1



def longest(n, edges):
    path = list(_order(n, edges))
    adjlist = defaultdict(list)
    for u,v in edges:
        adjlist[u].append(v)
        

    solution = defaultdict(lambda:[-1,0])
    #solution[u] = [u]
    maxN = -1
    for u in path:
        for v in adjlist[u]:
            if solution[u][1] + 1 > solution[v][1]:
                solution[v] = [u, solution[u][1] + 1]
                maxN = v
     
     
     
    m = solution[maxN][1]
    fPath = [maxN]
    for _ in range(solution[maxN][1]):
        fPath.append(solution[maxN][0])
        maxN = fPath[-1]
    
    
    return m, list(reversed(fPath))
    
    
    
    
print(longest(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
