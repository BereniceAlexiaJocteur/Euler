# -------------------------------------------------------------------------------
# Name:        pb216
# Purpose:     project euler
# Created:     13/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    resultat = 0

    for i in range(0, 50000000):
        if primes.is_prime_opti((2*(i**2))-1):
            resultat += 1

    print(resultat)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())