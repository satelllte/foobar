import solution

class Item:
    def __init__(self, h, q):
        self.h = h
        self.q = q

items = [
    Item(1, [1]),
    Item(2, [3, 2, 1]),
    Item(3, [7, 3, 5, 1]),
    Item(3, [7, 3, 4, 1]),
    Item(4, [7, 3, 4, 1]),
    Item(4, [9, 8, 15, 11, 12]),
    Item(4, [6, 7, 10, 14, 13]),
    Item(5, [19, 14, 28]),
    Item(5, [19, 15, 29]),
    Item(5, [28, 29, 16, 30, 31, 1, 4]),
    Item(30, [28, 29, 16, 30, 31, 1, 4]),
]

for item in items:
    print('h: {} | q: {} | result: {}'.format(item.h, item.q, solution.solution(item.h, item.q)))
