from year_2022.level_2.ion_flux_relabeling.solution import solution

def test():
    assert solution(1, [1]) == [-1]
    assert solution(2, [3, 2, 1]) == [-1, 3, 3]
    assert solution(3, [7, 3, 5, 1]) == [-1, 7, 6, 3]
    assert solution(3, [7, 3, 4, 1]) == [-1, 7, 6, 3]
    assert solution(4, [7, 3, 4, 1]) == [15, 7, 6, 3]
    assert solution(4, [9, 8, 15, 11, 12]) == [10, 10, -1, 13, 13]
    assert solution(4, [6, 7, 10, 14, 13]) == [7, 15, 14, 15, 14]
    assert solution(5, [19, 14, 28]) == [21, 15, 29]
    assert solution(5, [19, 15, 29]) == [21, 31, 30]
    assert solution(5, [28, 29, 16, 30, 31, 1, 4]) == [29, 30, 18, 31, -1, 3, 6]
    assert solution(30, [28, 29, 16, 30, 31, 1, 4]) == [29, 30, 18, 31, 63, 3, 6]
