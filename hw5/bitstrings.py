baseCase = {0:1, 1:2}
def num_no(n):
    if n in baseCase:
        return baseCase[n]

    a,b = 2,1
    for i in range(2, n+1):
        a,b = a+b, a
    return a


def num_yes(n):
    a,b = 0,0
    for i in range(2, n+1):
        a, b = a+b+(2**(i-2)), a
    return a
