from year_2022.level_3.doomsday_fuel.solution import solution

def test():
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

    assert solution([
        [0, 1],
        [0, 0],
    ]) == [1, 1]

    assert solution([
        [0, 0, 1],
        [0, 0, 0],
        [0, 0, 0],
    ]) == [0, 1, 1]

