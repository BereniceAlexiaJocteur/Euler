# -------------------------------------------------------------------------------
# Name:        pb146
# Purpose:     project euler
# Created:     10/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    lim = 150000000
    i = 10
    somme = 0

    while i <= lim:
        s = i ** 2
        if primes.is_prime_opti(s + 1) and primes.is_prime_opti(s + 3) and primes.is_prime_opti(s + 7) and \
                primes.is_prime_opti(s + 9) and primes.is_prime_opti(s + 13) and primes.is_prime_opti(s + 27) and not \
                primes.is_prime_opti(s + 11) and not primes.is_prime_opti(s + 17) and not primes.is_prime_opti(s + 21) \
                and not primes.is_prime_opti(s + 23):
            somme += i
        i += 10

    print(somme)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())