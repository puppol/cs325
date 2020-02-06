#!/usr/bin/env python3

import random, sys
from random import shuffle
random.seed(1325)


def sort(a):
    if a == []:
        return []
    pivot = a[0]
    left = [x for x in a if x < pivot]
    right = [x for x in a[1:] if x >= pivot]
    return [sort(left)] + [pivot] + [sort(right)]


def get_depth(tree):
    if tree == []:
        return 0,0
    if tree[0] == [] and tree[2] == []:
        return 1,0
    else:
        left_len, path_left = get_depth(tree[0])
        right_len, path_right = get_depth(tree[2])
    
        return max(left_len, right_len) + 1, max(path_left, path_right, left_len+right_len)

def longest(tree):
    if tree == []:
        return []
        
    return get_depth(tree)[1]
    
    
    
    
    
    
    
#    
#def sorted(tree):
#    return [] if tree == [] else sorted(tree[0]) + [tree[1]] + sorted(tree[2])
#
#if __name__ == '__main__':
#    print(longest([[], 1, []]))
#    print(longest([[[], 1, []], 2, [[], 3, []]]))
#    print(longest([[[[], 1, []], 2, [[], 3, []]], 4, [[[], 5, []], 6, [[], 7, [[], 9, []]]]]))
#    tree = sort(random.sample(range(100), 100))
#    print(longest(tree))
#    print(tree)
##
