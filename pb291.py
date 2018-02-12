# -------------------------------------------------------------------------------
# Name:        pb291
# Purpose:     project euler
# Created:     01/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    n = 1
    p = n**2 + (n+1)**2
    compteur = 0

    while p < 5*10**15:
        if primes.is_prime_opti(p):
            compteur += 1
        n += 1
        p = n**2 + (n+1)**2

    print(compteur)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())