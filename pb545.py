# -------------------------------------------------------------------------------
# Name:        pb545
# Purpose:     project euler
# Created:     01/02/2016
# -------------------------------------------------------------------------------

import primes
import sympy
import sys
import time


def solve(m):
    count = 1
    for i in range(2, 10**7):
        l = 1
        n = 308*i
        b = sympy.divisors(n)
        for j in b:
            if primes.is_prime_opti(j+1):
                l *= j+1
                if l > 20010:
                    break
        if l == 20010:
            count += 1
            if count == m:
                return n


def main():
    start = time.perf_counter()
    print(solve(10**5))
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
