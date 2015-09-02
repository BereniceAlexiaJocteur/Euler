# -------------------------------------------------------------------------------
# Name:
# Purpose:
# Created:
# -------------------------------------------------------------------------------

import fractions
import time
import sys


def main():
    n = 41
    start = time.perf_counter()
    som = fractions.Fraction(0)
    for i in range(n):
        prob = fractions.Fraction(1) - (fractions.Fraction(1) - fractions.Fraction(1, 2**i))**32
        som += prob
    print(round(float(som), 10))
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())