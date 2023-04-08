"""
Replication process
-------------------------

L                       R
          (1,1)
      (2,1) | (2,1)
(3,1) (2,3) | (3,2) (1,3)

The right side is just mirrored from left one,
so for each step (M,F) pair can be swapped - so `M` is always more than or equal to `F` 

-------------------------

To speed up the evaluation process,
floor(m/f) step size can be taken each step instead of incrementing the step by 1 each iteration.

"""

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
