def generate(c1, c2, bitlen):
    x = c1 & ~(2 ** bitlen)
    y = c2 & ~(2 ** bitlen)
    z = c1 >> 1
    w = c2 >> 1
    return \
        ( x & ~y & ~z & ~w) |\
        (~x &  y & ~z & ~w) |\
        (~x & ~y &  z & ~w) |\
        (~x & ~y & ~z &  w)

from collections import defaultdict
def build_map(n, nums):
    mapping = defaultdict(set)
    nums = set(nums)
    for i in range(2 ** (n + 1)):
        for j in range(2 ** (n + 1)):
            generation = generate(i, j, n)
            print('n = {} | generation({}, {}) = {}'.format(n, i, j, generation))
            if generation in nums:
                mapping[(generation, i)].add(j)
    return mapping

def answer(g):
    print('g: {}'.format(g))

    g = list(zip(*g)) # transpose
    print('g (transposed): {}'.format(g))

    nrows = len(g)
    ncols = len(g[0])

    # turn map into numbers
    nums = [sum([2 ** i if col else 0 for i, col in enumerate(row)]) for row in g]
    print('nums: {}'.format(nums))

    mapping = build_map(ncols, nums)
    print('mapping: {}'.format(mapping))

    preimage = {i: 1 for i in range(2 ** (ncols + 1))}
    print('preimage: {}'.format(preimage))

    for row in nums:
        next_row = defaultdict(int)
        for c1 in preimage:
            for c2 in mapping[(row, c1)]:
                next_row[c2] += preimage[c1]
        preimage = next_row
    print('preimage (flattened): {}'.format(preimage))
    ret = sum(preimage.values())
    print('ret: {}'.format(ret))

    return ret
