def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def is_power_of_two(x):
    return x & (x - 1) == 0

def is_infinite_pair_naive(x, y):
    if x > y:
        x, y = y, x

    if x == y:
        return False

    pairs = {(x, y)}

    while True:
        y -= x
        x *= 2

        if x > y:
            x, y = y, x
        
        if x == y:
            return False
        
        if (x, y) in pairs:
            return True
        
        pairs.add((x, y))

def is_infinite_pair(x, y):
    return not is_power_of_two((x + y) / gcd(x, y))

def solution(banana_list):
    return 13183
