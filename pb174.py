# -------------------------------------------------------------------------------
# Name:        pb174
# Purpose:     project euler
# Created:     20/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    resultat = 0
    tableau = [0] * 1000001

    for i in range(1, 250001):
        h = 4 * i + 4
        j = i
        while h <= 1000000 and j >= 1:
            tableau[h] += 1
            j -= 2
            h += 4 * j + 4

    for x in tableau:
        if x in range(1, 11):
            resultat += 1

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())