def solution(n):
    n = int(n)

    count = 0
    cache = {n}
    items = {n}

    while not 1 in items:
        next_items = set()

        for x in items:
            if x % 2 == 0:
                if not x / 2 in cache:
                    next_items.add(x / 2)
                    cache.add(x / 2)
            else:
                if not x + 1 in cache:
                    next_items.add(x + 1)
                    cache.add(x + 1)
                if not x - 1 in cache:
                    cache.add(x - 1)
                    next_items.add(x - 1)

        items = next_items
        count = count + 1

    return count
