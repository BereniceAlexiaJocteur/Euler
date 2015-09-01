# -------------------------------------------------------------------------------
# Name:        pb183
# Purpose:     project euler
# Created:     21/08/2015
# -------------------------------------------------------------------------------

import fractions
import math
import time
import sys


def is_terminating(p, q):
    d = fractions.gcd(p, q)
    q //= d
    while q % 2 == 0:
        q //= 2
    while q % 5 == 0:
        q //= 5
    return q == 1


def function_d(n):
    k1 = n // math.e
    k2 = k1 + 1
    if (k1 * (math.log(n) - math.log(k1))) < (k2 * (math.log(n) - math.log(k2))):
        k = k2
    else:
        k = k1
    if is_terminating(n, k):
        return -n
    else:
        return n


def main():
    start = time.perf_counter()
    somme = 0
    i = 5

    while i < 10001:
        somme += function_d(i)
        i += 1

    print(somme)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())