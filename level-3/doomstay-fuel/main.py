from solution2 import solution
import foreign
import sol

items = [
    [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]],
    [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]],
    [[0]],
    # [[1]],
    [
        [0, 1],
        [0, 0],
    ],
    [
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0]
    ],
    [
        [0, 0, 0],
        [1, 0, 2],
        [0, 0, 0]
    ],
]

for m in items:
    print('m: {} \nresult: {}\n-----------'.format(m, solution(m)))
    print('m: {} \nresult: {}\n-----------'.format(m, sol.solution(m)))
    # print('m: {} \nresult: {}\n-----------'.format(m, foreign.solution(m)))

assert solution(
    [
        [0, 2, 1, 0, 0],
        [0, 0, 0, 3, 4],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
    ]
) == [7, 6, 8, 21]

assert solution(
    [
        [0, 1, 0, 0, 0, 1],
        [4, 0, 0, 3, 2, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0],
    ]
) == [0, 3, 2, 9, 14]

assert solution([
    [0],
]) == [1, 1]

# assert solution([
#     [0, 1],
#     [0, 0],
# ]) == [1, 1]

# assert solution([
#     [0, 0, 1],
#     [0, 0, 0],
#     [0, 0, 0],
# ]) == [0, 1, 1]
