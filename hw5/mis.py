def max_wis(a, wis = None):
    if wis == None:
        wis = {}
    a_len = len(a)
    if a_len in wis:
        return wis[a_len]
    if a == []:
        return 0,[]
    if a_len == 1:
        if max(a[0], 0) == 0:
            return 0,[]
        return a[0], a

    w1, list1 = max_wis(a[:-1],wis)
    w2, list2 = max_wis(a[:-2],wis)
    w2 =  w2 + a[-1]
    if w2 > w1:
        wis[a_len] = w2, list2 + a[-1:]
    else:
        wis[a_len] =  w1, list1

    return wis[a_len]


def max_wis2(a):
    wis = {}
    if a == []:
        return 0,[]
    wis[0] = 0,[]
    wis[1] = (a[0], [a[0]]) if a[0] > 0 else (0,[])
    len_a = len(a)

    for i in range(1,len_a):
        print(wis[i])
        t = (a[i], [a[i]]) if a[i] > 0 else (0,[])
        v = wis[i-1][0] + t[0]
        if v > wis[i][0]:
            wis[i+1] = v, wis[i-1][1] + t[1]
        else:
            wis[i+1] = wis[i]
    return wis[len_a]
