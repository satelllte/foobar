# Tree part:
#
#   P
#  / \
# L   R
# 
# If H is the tree height on the level of P, then:
#
# P = 2^H - 1
# L = P - 2^(H-1)
# R = P - 1
# 
# When searching a number above node X on the level H:
#
# if X >= P             ---> the answer is -1 (no levels above)
# if X = L or X = R     ---> the answer is P
# if X < L              ---> go deep to the left
# if X > L              ---> go deep to the right
# 
# Example:
#
# | --------------------------- |
# | Level (H) |     Nodes       |
# | --------- | --------------- |
# |     3     |        7        |
# |     2     |    3       6    |
# |     1     |  1   2   4   5  |
# | --------------------------- |

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
    return list(map(lambda x: solve(h, p, x), q))
