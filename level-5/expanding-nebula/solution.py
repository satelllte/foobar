from collections import defaultdict

def get_number_from_bits(bits):
    number_parts = []
    for i, b in enumerate(bits):
        if b:
            number_parts.append(2 ** i)
    return sum(number_parts)

def get_numbers_from_grid(grid):
    numbers = []
    for bits in grid:
        numbers.append(get_number_from_bits(bits))
    return numbers

def calculate_generation(a, b, bit_count):
    x = a & ~(2 ** bit_count)
    y = b & ~(2 ** bit_count)
    z = a >> 1
    w = b >> 1
    return \
        ( x & ~y & ~z & ~w) |\
        (~x &  y & ~z & ~w) |\
        (~x & ~y &  z & ~w) |\
        (~x & ~y & ~z &  w)

def get_mapping(n, numbers):
    numbers_set = set(numbers)
    mapping = defaultdict(set)
    for i in range(2 ** (n + 1)):
        for j in range(2 ** (n + 1)):
            generation = calculate_generation(i, j, n)
            if generation in numbers_set:
                mapping[(generation, i)].add(j)
    return mapping

def get_base_preimage(n):
    return { i: 1 for i in range(2 ** (n + 1)) }

def filter_preimage(preimage, numbers, mapping):
    for row in numbers:
        next_row = defaultdict(int)
        for a in preimage:
            for b in mapping[(row, a)]:
                next_row[b] += preimage[a]
        preimage = next_row
    return preimage

def get_preimage_sum(preimage):
    return sum(preimage.values())

def solution(grid):
    grid = zip(*grid)
    cols_count = len(grid[0])
    numbers = get_numbers_from_grid(grid)
    mapping = get_mapping(cols_count, numbers)
    preimage = get_base_preimage(cols_count)
    preimage = filter_preimage(preimage, numbers, mapping)
    return get_preimage_sum(preimage)
