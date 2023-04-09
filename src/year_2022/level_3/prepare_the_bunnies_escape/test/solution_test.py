from year_2022.level_3.prepare_the_bunnies_escape.solution import solution

def test():
    assert solution([
        [0, 1, 1, 0],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
        [1, 1, 1, 0],
    ]) == 7

    assert solution([
        [0, 0, 0, 0, 0, 0], 
        [1, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0], 
        [0, 1, 1, 1, 1, 1], 
        [0, 1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 0],
    ]) == 11

    assert solution([
        [0, 0],
        [0, 0],
    ]) == 3

    assert solution([
        [0, 1],
        [0, 0],
    ]) == 3

    assert solution([
        [0, 0],
        [1, 0],
    ]) == 3

    assert solution([
        [0, 1],
        [1, 0],
    ]) == 3

    assert solution([
        [0, 1, 0],
        [1, 0, 0],
    ]) == 4

    assert solution([
        [0, 0, 1],
        [1, 1, 0],
    ]) == 4

    assert solution([
        [0, 0, 1],
        [1, 1, 0],
        [1, 1, 0],
    ]) == 5

    assert solution([
        [0, 0, 1, 1],
        [1, 1, 0, 0],
        [1, 1, 0, 0],
    ]) == 6
