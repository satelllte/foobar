from solution import solution

items = [
    '1',
    '2',
    '3',
    '4',
    '5',
    '6',
    '7',
    '8',
    '9',
    '15',
    '155',
    '124894',
    '91124894',
    '491124894',
]

for n in items:
    print('n: {} \nresult: {}\n-----------'.format(n, solution(n)))
