# -------------------------------------------------------------------------------
# Name:        pb80
# Purpose:     project euler
# Created:     13/07/2015
# -------------------------------------------------------------------------------

import bigfloat
import time
import sys


def partie_decimale(n):
    u = int(n)
    l = len(str(u))
    return str(u)+str(n)[l+1:]


def sumdigits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def main():
    start = time.perf_counter()
    somme = 0

    for i in range(1, 101):
        rac = bigfloat.sqrt(i, bigfloat.precision(385))
        if rac != int(rac):
            s = partie_decimale(rac)[:100]
            somme += sumdigits(int(s))

    print(somme)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())