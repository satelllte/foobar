from solution import solution

items = [
    ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"],
    ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"],
    ["99.0.0", "99.11", "99.11.0", "100.0", "100.0.0", "100", "100.1.0", "100.1.1", "100.1", "99"],
]

for versions in items:
    print('versions: {} \nresult: {}\n-----------'.format(versions, solution(versions)))
