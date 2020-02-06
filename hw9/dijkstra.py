from heapdict import heapdict
from collections import defaultdict

def shortest(n, e):
    graph = defaultdict(list)
    heap = heapdict()
    blacked = set()
    trace = {}
    heap[0] = 0
    
    for n1, n2, weight in e:
        graph[n1].append([n2, weight])
        graph[n2].append([n1, weight])
 
#    print(graph)
    
    final_node = (None, None)
    while heap:
        curr_node = heap.popitem()
        
        if curr_node[0] == n-1:
            final_node = curr_node
            break
        blacked.add(curr_node[0])
        for node, weight in graph[curr_node[0]]:
            if node not in blacked:
                possible_weight = weight + curr_node[1]
                if not node in heap or heap[node] > possible_weight:
                    trace[node] = curr_node[0]
                    heap[node] = possible_weight
         
         
    if final_node[0]:
        path = [final_node[0]]
        t = final_node[0]
        while path[-1] is not 0:
            path.append(trace[t])
            t = path[-1]
        return final_node[1],list(reversed(path))
    return None




print(shortest(4, [(0,1,1), (0,2,5), (1,2,1), (2,3,2), (1,3,6)]))
