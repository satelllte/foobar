def solution(m, f):
    m = int(m)
    f = int(f)
    step = 0

    while m > 0 and f > 0:
        step += 1

        if m < f: m, f = f, m
        m -= f

        if m == 1 and f == 1:
            return '{}'.format(step)

    return 'impossible'
