# -------------------------------------------------------------------------------
# Name:        pb140
# Purpose:     project euler
# Created:     22/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def a(n, x0, y0, t=set()):
    if n == 0:
        return x0, y0, t
    else:
        x = -9 * a(n-1, x0, y0)[0] + 20 * a(n-1, x0, y0)[1] + 28
        y = 4 * a(n-1, x0, y0)[0] - 9 * a(n-1, x0, y0)[1] - 14
        if y > 0:
            t.add(y)
        return x, y, t


def main():
    start = time.perf_counter()
    s = [(-1, 0), (1, 0), (-7, 2), (7, 2), (-2, -3), (2, -3), (-5, -4), (5, -4), (14, 5)]
    solutions = set()
    resultat = 0

    for k in range(len(s)):
        x1 = s[k][0]
        y1 = s[k][1]
        solutions = solutions | a(10, x1, y1)[2]

    solutions = sorted(list(solutions))

    for k in range(30):
        resultat += solutions[k]

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())