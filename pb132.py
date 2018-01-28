# -------------------------------------------------------------------------------
# Name:        pb132
# Purpose:     project euler
# Created:     05/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    p = primes.primes(160001)
    result = 0
    count = 0
    i = 3

    while count < 40:
        if pow(10, 10**9, 9 * p[i]) == 1:
            count += 1
            result += p[i]
        i += 1

    print(result)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())