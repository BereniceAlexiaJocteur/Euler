# -------------------------------------------------------------------------------
# Name:        pb127
# Purpose:     project euler
# Created:     24/08/2015
# -------------------------------------------------------------------------------

import fractions
import time
import sys


def main():
    start = time.perf_counter()
    somme = 0
    radicals = [1] * 120001

    for i in range(2, 120000):
        if radicals[i] == 1:
            for j in range(i, 120000, i):
                radicals[j] *= i

    for c in range(3, 120000):
        if 2 * radicals[c] >= c:
            continue
        for a in range(1, c//2):
            b = c - a
            if radicals[a]*radicals[b]*radicals[c] < c and fractions.gcd(a, b) == 1:
                somme += c

    print(somme)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())