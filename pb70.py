# -------------------------------------------------------------------------------
# Name:        pb70
# Purpose:     project euler
# Created:     15/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def is_perm(a, b):
    return sorted(str(a)) == sorted(str(b))


def main():
    start = time.perf_counter()
    p = primes.primes(5000011)
    minimum = 87109 / 79180
    ind = 87109

    for i in range(len(p)):
        j = 0
        while p[i] * p[j] < 10000000:
            t = (p[i]-1) * (p[j]-1)
            n = p[i] * p[j]
            if is_perm(t, n):
                if n / t < minimum:
                    minimum = n / t
                    ind = n
            j += 1

    print(ind)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())