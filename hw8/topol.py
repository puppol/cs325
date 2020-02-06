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
        

order = lambda n, edges: list(_order(n, edges))



print(order(8, [(0,2), (1,2), (2,3), (2,4), (3,4), (3,5), (4,5), (5,6), (5,7)]))
print(order(4, [(0,1), (1,2), (2,1), (2,3)]))
print(order(5, [(0,1), (1,2), (2,3), (3,4)]))
print(order(5, []))
print(order(1, [(0,0)])) # self-loop
