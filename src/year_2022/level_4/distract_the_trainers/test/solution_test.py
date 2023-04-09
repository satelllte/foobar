from year_2022.level_4.distract_the_trainers.solution import solution

def test():
    assert solution([1, 7, 3, 21, 13, 19]) == 0
    assert solution([7, 1, 3, 21, 13, 19]) == 0
    assert solution([7, 3, 1, 21, 13, 19]) == 0
    assert solution([7, 3, 1, 13, 19, 21]) == 0
    assert solution([1, 7, 3, 21, 13, 19, 1]) == 1
    assert solution([1, 1, 7, 3, 21, 13, 19]) == 1

    assert solution([1,1,1,2]) == 2

    assert solution([1, 1]) == 2
    assert solution([2, 2]) == 2
    assert solution([3, 3]) == 2
    assert solution([19, 19]) == 2
    assert solution([19214, 19214]) == 2
    assert solution([1073741822, 1073741822]) == 2
    assert solution([1073741823, 1073741823]) == 2

    assert solution([3, 3, 3, 3]) == 4
    assert solution([27000, 27000, 27000, 27000]) == 4

    assert solution([3, 3, 3, 3, 3]) == 5
    assert solution([6, 6, 6, 6, 6]) == 5

    assert solution([1, 4]) == 0
    assert solution([4, 1]) == 0

    assert solution([3, 5]) == 2
    assert solution([5, 3]) == 2

    assert solution([3, 5, 5, 3, 5]) == 5
    assert solution([3, 5, 5, 3]) == 4
    assert solution([3, 5, 5, 3, 5, 3, 3, 5]) == 8

    assert solution([2,2,2]) == 3
    assert solution([2,2,4]) == 1
    assert solution([2,4,2]) == 1
    assert solution([4,2,2]) == 1
    assert solution([2,2,2,2,4]) == 3
    assert solution([2,4,2,2,2]) == 3
    assert solution([2,4,2,2,2,2]) == 4
