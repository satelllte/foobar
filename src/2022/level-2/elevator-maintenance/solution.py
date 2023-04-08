import re
import functools

regexX = re.compile(r'^(\d+)$')
regexXY = re.compile(r'^(\d+)\.(\d+)$')
regexXYZ = re.compile(r'^(\d+)\.(\d+)\.(\d+)$')

def parse(version):
    x = -1
    y = -1
    z = -1

    matchX = regexX.search(version)
    matchXY = regexXY.search(version)
    matchXYZ = regexXYZ.search(version)

    if matchX:
        x = int(matchX.group())
    elif matchXY:
        x, y = map(int, matchXY.groups())
    elif matchXYZ:
        x, y, z = map(int, matchXYZ.groups())
    
    return (x, y, z)

def compare(a, b):
    x1, y1, z1 = parse(a)
    x2, y2, z2 = parse(b)

    if x1 > x2: return 1
    elif x1 < x2: return -1
    else:
        if y1 > y2: return 1
        elif y1 < y2: return -1
        else:
            if z1 > z2: return 1
            elif z1 < z2: return -1
            else: return 0

def solution(l):
    return sorted(l, key=functools.cmp_to_key(compare))

