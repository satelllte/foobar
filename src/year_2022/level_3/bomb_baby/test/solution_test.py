from year_2022.level_3.bomb_baby.solution import solution

def test():
    assert solution('4', '7') == '4'
    assert solution('2', '1') == '1'
    assert solution('2', '2') == 'impossible'
    assert solution('2', '4') == 'impossible'
    assert solution('5', '3') == '3'
    assert solution('1', '4') == '3'
    assert solution('1122737776', '2838294894288') == 'impossible'
