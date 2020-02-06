def best(bagSize, bagPairs, bagSet = None):
    if bagSet is None:
        bagSet = {}
        bagSet[0] = (0,[0 for _ in range(len(bagPairs))])

    if bagSize <= 0:
        return bagSet[0]

    if bagSize in bagSet:
        return bagSet[bagSize]

    for i,pair in enumerate(bagPairs):
        bagRemain = bagSize - pair[0]
        if bagRemain < 0:
            bagSet[bagSize] = bagSet[0]
            continue
        val, nSet = best(bagRemain, bagPairs, bagSet)
        if bagSize in bagSet:
            if val + pair[1] > bagSet[bagSize][0]:
                bagSet[bagSize] = (val + pair[1], [x if j != i else x+1 for j,x in enumerate(nSet)])
        else:
            bagSet[bagSize] = (val + pair[1], [x if j != i else x+1 for j,x in enumerate(nSet)])

    return bagSet[bagSize]



print(best(3, [(2, 4), (3, 5)]))
print(best(3, [(1, 5), (1, 5)]))
print(best(3, [(1, 2), (1, 5)]))
print(best(3, [(1, 2), (2, 5)]))
print(best(58, [(5, 9), (9, 18), (6, 12)]))
print(best(92, [(8, 9), (9, 10), (10, 12), (5, 6)]))

