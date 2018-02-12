# -------------------------------------------------------------------------------
# Name:        pb133
# Purpose:     project euler
# Created:     06/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def main():
    start = time.perf_counter()
    p = primes.primes(10**5)
    somme = 0

    for i in p:
        test = True
        for n in range(1, 17):
            if pow(10, 10**n, 9*i) == 1:
                test = False
                break
        if test:
            somme += i

    print(somme)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())