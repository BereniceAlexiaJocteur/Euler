# -------------------------------------------------------------------------------
# Name:        pb128
# Purpose:     project euler
# Created:     29/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    compteur = 2
    r = 0

    while compteur < 2000:
        r += 1
        if primes.is_prime_opti(6*r+7) and primes.is_prime_opti(12*r+17) and primes.is_prime_opti(6*r+5):
            compteur += 1
        if primes.is_prime_opti(12*r+5) and primes.is_prime_opti(6*r+5) and primes.is_prime_opti(6*r+11):
            compteur += 1

    if compteur == 2001:
        print(3*r**2+3*r+2)
    elif primes.is_prime_opti(6*r+7) and primes.is_prime_opti(12*r+17) and primes.is_prime_opti(6*r+5):
        print(3*r**2+3*r+2)
    else:
        print(3*r**2+9*r+7)

    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())