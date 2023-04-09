from year_2022.level_3.fuel_injection_perfection.solution import solution

def test():
    assert solution(1) == 0
    assert solution(2) == 1
    assert solution(3) == 2
    assert solution(4) == 2
    assert solution(5) == 3
    assert solution(6) == 3
    assert solution(7) == 4
    assert solution(8) == 3
    assert solution(9) == 4
    assert solution(15) == 5
    assert solution(155) == 10
    assert solution(124894) == 21
    assert solution(91124894) == 36
    assert solution(491124894) == 38
