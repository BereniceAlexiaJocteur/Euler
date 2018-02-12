# -------------------------------------------------------------------------------
# Name:        pb278
# Purpose:     project euler
# Created:     24/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    p = primes.primes(5000)
    somme = 0

    for r in range(2, len(p)):
        pr = p[r]
        for q in range(1, r):
            pq = p[q]
            temp = pr*pq
            temp1 = 2*temp - pr - pq
            for p1 in range(q):
                somme += p[p1]*temp1 - temp

    print(somme)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())