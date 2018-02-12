# -------------------------------------------------------------------------------
# Name:        pb193
# Purpose:     project euler
# Created:     28/08/2015
# -------------------------------------------------------------------------------

import math
import time
import sys


def mobius_sieve(lim):
    sqrt = math.floor(math.sqrt(lim))
    mu = [1] * (lim + 1)
    for i in range(2, sqrt+1):
        if mu[i] == 1:
            for j in range(i, lim+1, i):
                mu[j] *= -i
            for j in range(i*i, lim+1, i*i):
                mu[j] = 0
    for i in range(2, lim+1):
        if mu[i] == i:
            mu[i] = 1
        elif mu[i] == -i:
            mu[i] = -1
        elif mu[i] < 0:
            mu[i] = 1
        elif mu[i] > 0:
            mu[i] = -1
    return mu


def main():
    start = time.perf_counter()
    mob = mobius_sieve(2**25)
    res = 0

    for k in range(1, 2**25):
        res += mob[k]*(2**50//k**2)

    print(res)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())