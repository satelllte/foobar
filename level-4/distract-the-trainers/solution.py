import numpy as np

def is_power_of_two(x):
    return x & (x - 1) == 0

def is_infinite_pair(x, y):
    return not is_power_of_two((x + y) / np.gcd(x, y))

def solution_old(items):
    items = sorted(items)

    row_indexes = set()
    col_indexes = set()

    for i in range(len(items)):
        for j in range(i, len(items)):
            if i == j:
                continue
            if is_infinite_pair(items[i], items[j]):
                row_indexes.add(i)
                col_indexes.add(j)

    pair_count = min(len(row_indexes), len(col_indexes))
    if pair_count * 2 > len(items):
        pair_count -= 1

    result = len(items) - pair_count * 2

    return result

def solution(items):
    return solution_old(items)
