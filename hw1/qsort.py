


def sort(a):
    if a == [] or len(a) == 1:
        return a
    else:
        pivot = a[0]
        left  = [x for x in a if x < pivot]
        right = [x for x in a[1:] if x >= pivot]
        return [sort(left)] + [pivot] + [sort(right)]


# [[[1], 2, [3]], 4, [[5], 6, [[], 7, [9]]]]
#  [[1], 2, [3]], 4, [[5], 6, [[], 7, [9]]]
#   [1], 2, [3]
#    1   2   3

#                 4  [5], 6, [[], 7, [9]]
#                     5   6   []  7  [9]
#                             7   9

def sorted(tree):
    if tree == []:
        return tree
    if isinstance(tree[0], list):
        return sorted(tree[0]) + sorted(tree[1:])
    return tree[:1] + sorted(tree[1:])
    
    
    
def search(tree, value):
    return value in sorted(tree)
    
  
def insert(tree, value):
    if not search(tree, value):
        tree = sorted(tree)
        tree.append(value)
        return sort(tree)
