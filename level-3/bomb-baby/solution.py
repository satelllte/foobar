def solution(m, f):
    IMPOSSIBLE = 'impossible'

    m = int(m)
    f = int(f)
    step = 0

    while m > 0 and f > 0:
        if m == 1 and f == 1:
            return '{}'.format(step)

        if m < f:
            m, f = f, m
        
        step_delta = int(m / f) if f > 1 else int(m / f) - 1
        step += step_delta
        m -= step_delta * f

    return IMPOSSIBLE
