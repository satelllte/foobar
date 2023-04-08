import math

def solution(area):
    panels = []

    while area > 0:
        x = int(math.floor(math.sqrt(area)))
        x_sqr = x * x
        area = area - x_sqr
        panels.append(x_sqr)

    return panels
