# Technique used: https://en.wikipedia.org/wiki/Beatty_sequence

import decimal

def solution(str_n):
    n = int(str_n)
    n = decimal.Decimal(n)

    with decimal.localcontext() as decimal_ctx:
        decimal_ctx.prec = 101

        sqrt2 = decimal.Decimal(2).sqrt()
        sqrt2plus2 = sqrt2 + decimal.Decimal(2)

        def solve(n):
            if n <= 0:
                return 0
            bn = int(sqrt2 * n)
            bs = int(decimal.Decimal(bn) / sqrt2plus2)
            return ((bn * (bn + 1)) / 2) - solve(bs) - (bs * (bs + 1))

        return str(int(solve(n)))
