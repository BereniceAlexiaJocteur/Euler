# -------------------------------------------------------------------------------
# Name:        pb108
# Purpose:     project euler
# Created:     17/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def num_div_of_square(n):
    temp = n
    resultat = 1
    primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
    for i in primes:
        compteur = 0
        while temp % i == 0:
            temp //= i
            compteur += 1
        resultat *= compteur * 2 + 1
        if compteur == 0:
            break
    return resultat


def main():
    start = time.perf_counter()
    j = 4

    while num_div_of_square(j) < 2000:
        j += 1

    print(j)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())