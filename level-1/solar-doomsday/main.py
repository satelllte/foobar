import solution

areas = [
  1,
  2,
  3,
  4,
  5,
  7,
  9,
  10,
  12,
  13,
  1000,
  1001,
  15324,
  128399,
  1000000,
]

for area in areas:
    print('area: {} | solution: {}'.format(area, solution.solution(area)))
