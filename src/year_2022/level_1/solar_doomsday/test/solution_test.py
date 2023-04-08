from year_2022.level_1.solar_doomsday.solution import solution

def test():
    assert solution(1) == [1]
    assert solution(2) == [1, 1]
    assert solution(3) == [1, 1, 1]
    assert solution(4) == [4]
    assert solution(5) == [4, 1]
    assert solution(7) == [4, 1, 1, 1]
    assert solution(9) == [9]
    assert solution(10) == [9, 1]
    assert solution(12) == [9, 1, 1, 1]
    assert solution(13) == [9, 4]
    assert solution(1000) == [961, 36, 1, 1, 1]
    assert solution(1001) == [961, 36, 4]
    assert solution(15324) == [15129, 169, 25, 1]
    assert solution(128399) == [128164, 225, 9, 1]
    assert solution(1000000) == [1000000]
