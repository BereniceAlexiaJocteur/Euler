# -------------------------------------------------------------------------------
# Name:        pb88
# Purpose:     project euler
# Created:     14/02/2015
# -------------------------------------------------------------------------------

import time
import sys


def gen(maxprod, start=2):
    for i in range(start, maxprod + 1):
        yield (i,)
    for i in range(start, int(maxprod ** 0.5) + 1):
        for g in gen(maxprod // i, i):
            yield (i,) + g


def product(p):
    prod = 1
    for x in p:
        prod *= x
    return prod


def main():
    startt = time.perf_counter()
    n = 24000
    a = [2 * n + 1] * (n + 1)
    a[1] = 1
    b = set([])

    for v in gen(2 * n):
        pi = product(v)
        k = pi - sum(v) + len(v)
        if k <= n and a[k] > pi:
            a[k] = pi

    for k in range(2, n // 2 + 1):
        b.add(a[k])

    print(sum(i for i in b))
    print('temps d\'exécution', time.perf_counter() - startt, 'sec')

if __name__ == '__main__':
    sys.exit(main())