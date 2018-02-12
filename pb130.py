# -------------------------------------------------------------------------------
# Name:        pb130
# Purpose:     project euler
# Created:     06/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def testa(n):
    u = 1
    i = 1
    while u and i <= n:
        u = (u * 10 + 1) % n
        i += 1
    if i > n:
        return False
    elif (n-1) % i == 0:
        return True
    else:
        return False


def main():
    start = time.perf_counter()
    compteur = 5
    ind = 703
    som = 91 + 259 + 451 + 481 + 703

    while compteur < 25:
        ind += 2
        if ind % 5 != 0 and not primes.is_prime(ind) and testa(ind):
            compteur += 1
            som += ind

    print(som)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())