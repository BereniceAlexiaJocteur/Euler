# -------------------------------------------------------------------------------
# Name:        pb231
# Purpose:     project euler
# Created:     18/07/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    p = primes.sieve8(20000000)
    resultat = 0

    for i in p:
        pi = i
        while pi <= 20000000:
            resultat += i * (20000000//pi - 15000000//pi - (20000000 - 15000000)//pi)
            pi *= i

    print(resultat)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())