def best(bagSize, bagPairs):
    # s = time.time()
    og = [list(e) for e in bagPairs]
    bPairs = []
    for x,y,z in bagPairs:
        bPairs.extend([(x,y) for _ in range(z)])

    tSum = len(bPairs)

    array = [[0] * (bagSize+1) for _ in range(tSum + 1)]
    backTrace = [[0] *(bagSize+1) for _ in range(tSum + 1)]

    # print(time.time() - s)
    # s = time.time()

    for w in range(1,bagSize + 1):
        for pair in range(1,tSum + 1):
            dif = w - bPairs[pair-1][0]
            if dif >= 0:
                a,b = bPairs[pair-1][1] + array[pair-1][dif], array[pair-1][w]
                if a > b:
                    array[pair][w] = a
                    backTrace[pair][w] = dif + w
                else:
                    array[pair][w] = b

                #
                # array[pair][w] = max(bPairs[pair-1][1] + array[pair-1][dif], array[pair-1][w])
                # # Check for backtrace
                # if array[pair][w] != array[pair-1][w]:
                #     backTrace[pair][w] = dif + w

    # print(time.time() - s)
    # s = time.time()
    pSet = []
    w = bagSize
    pair = tSum
    while w > 0 and pair > 0:
        if backTrace[pair][w] == 0:
            pair -= 1
        else:
            pSet.append(bPairs[pair-1])
            w -= bPairs[pair-1][0]
            pair -= 1

    for v in pSet:
        for i in og:
            if v[0] == i[0] and v[1] == i[1] and i[2] > 0:
                i[2] -= 1
                break
    f = [bagPairs[i][2] - og[i][2] for i in range(len(og))]
    # print(time.time() - s)
    return (array[tSum][bagSize], f)
