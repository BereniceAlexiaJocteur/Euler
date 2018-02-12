# -------------------------------------------------------------------------------
# Name:        pb131
# Purpose:     project euler
# Created:     31/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    n = 1
    p = 1 + 3*(n-1)*n
    compteur = 0

    while p < 1000000:
        if primes.is_prime(p):
            compteur += 1
        n += 1
        p = 1 + 3*(n-1)*n

    print(compteur)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())