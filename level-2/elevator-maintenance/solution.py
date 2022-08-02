import re

def solution(l):

    regexXYZ = re.compile(r'^(\d+)\.(\d+)\.(\d+)$')
    regexXY = re.compile(r'^(\d+)\.(\d+)$')
    regexX = re.compile(r'^(\d+)$')

    for version in l:
        print('version: {}'.format(version))
        matchXYZ = regexXYZ.search(version)
        matchXY = regexXY.search(version)
        matchX = regexX.search(version)
        if matchXYZ:
            x, y, z = map(int, matchXYZ.groups())
            print('matchXYZ: {} | {} | {}'.format(x, y, z))
        elif matchXY:
            x, y = map(int, matchXY.groups())
            print('matchXY: {} | {}'.format(x, y))
        elif matchX:
            x = int(matchX.group())
            print('matchX: {}'.format(x))

    return 1
