# -------------------------------------------------------------------------------
# Name:        pb191
# Purpose:     project euler
# Created:     26/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def f(n, l):
    return l[n+3]


def main():
    start = time.perf_counter()
    a = [0] * 34
    a[2] = 1

    for i in range(3, 34):
        a[i] = a[i-1] + a[i-2] + a[i-3]

    resultat = f(29, a)

    for j in range(1, 15):
        resultat += f(j, a) * f(29-j, a)

    resultat *= 2
    resultat += f(30, a)

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())