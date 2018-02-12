# -------------------------------------------------------------------------------
# Name:        pb123
# Purpose:     project euler
# Created:     16/02/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def reste(n, pr):
    p = pr[n-1]
    p2 = p**2
    return (pow(p-1, n, p2) + pow(p+1, n, p2)) % p2


def main():
    start = time.perf_counter()
    test = 1
    k = 1
    pri = primes.primes(1000000)

    while test:
        k += 1
        if reste(k, pri) > 10**10:
            test = False

    print(k)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())