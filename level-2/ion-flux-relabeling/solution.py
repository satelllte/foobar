def solve(h, p, x):
    if x >= p:
        return -1

    l = p - 2 ** (h - 1)
    r = p - 1

    if x == l or x == r:
        return p

    if x < l:
        return solve(h - 1, l, x)

    if x > l:
        return solve(h - 1, r, x)

def solution(h, q):
    p = 2 ** h - 1
    return map(lambda x: solve(h, p, x), q)
