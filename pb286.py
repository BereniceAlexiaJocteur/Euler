# -------------------------------------------------------------------------------
# Name:        pb286
# Purpose:     project euler
# Created:     26/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def probability(q):
    scoring = [0.0] * 51
    scoring[0] = 1.0
    for x in range(1, 51):
        next_scoring = [0.0] * 51
        next_scoring[0] = scoring[0] * x/q
        for y in range(1, 51):
            next_scoring[y] = scoring[y-1] * (1 - x/q) + scoring[y] * x/q
        scoring = next_scoring
    return scoring[20]


def main():
    start = time.perf_counter()
    a, b, epsilon = 50.1, 60.0, 10e-15

    for i in range(100):
        m = (a + b)/2
        p = probability(m)
        if abs(p - 0.02) < epsilon:
            print('%.10f' % m)
            break
        elif p > 0.02:
            a = m
        else:
            b = m

    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())