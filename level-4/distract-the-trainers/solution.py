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

def exclude_unpaired_items(items):
    paired_items = []
    for i in range(len(items)):
        for j in range(len(items)):
            if i == j:
                continue
            if is_infinite_pair(items[i], items[j]):
                paired_items.append(items[i])
                break
    return paired_items

def compute_min_pairs(items, passed = set()):
    # print('passed: {}', passed)

    # passed = {i, j}
    min_passed = len(items) - len(passed)
    for i in range(len(items)):
        # print('passed: {}'.format(passed))
        # print('len passed: {}'.format(len(passed)))
        if i in passed:
            continue

        row_passed = False

        for j in range(i, len(items)):
            if i == j:
                continue
            if is_infinite_pair(items[i], items[j]):
                row_passed = True

                # print('pair -> ({}, {})'.format(items[i], items[j]))
                passed_copy = passed.copy()
                passed_copy.add(i)
                passed_copy.add(j)
                l = len(passed_copy)
                x = compute_min_pairs(items, passed_copy)
                # print('pair ({}, {}) | min_items: {}'.format(items[i], items[j], x))
                if x < min_passed:
                    min_passed = x
                if min_passed == 0:
                    return min_passed
                # passed.add(i)
                # passed.add(j)
                # break
        
        if row_passed:
            break
    # print('FINAL min_passed: {}'.format(min_passed))
    # print('FINAL len passed: {}'.format(len(passed)))
    # return len(items) - len(passed)
    return min_passed


def solution(items):
    paired_items = exclude_unpaired_items(items)
    
    return compute_min_pairs(items)

    # for i in range(len(items)):
    #     for j in range(i, len(items)):
    #         if i == j:
    #             continue

    #         print('pos: ({}, {}) | pair: ({}, {}) | is_infinite_pair: {}'.format(i, j, items[i], items[j], is_infinite_pair(items[i], items[j])))

    #         if is_infinite_pair(items[i], items[j]):
    #             x = compute_min_pairs(items, {i, j})
    #             print('x = {}'.format(x))

    return 13183
