def bsts(n):
    if n <= 1:
        return 1
    a = 0
    for i in range(n):
        a += bsts(i) * bsts(n-i-1)
    return a
