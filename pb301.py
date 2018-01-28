# -------------------------------------------------------------------------------
# Name:        pb301
# Purpose:     project euler
# Created:     21/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    resultat = 0

    for n in range(1, 2**30 + 1):
        a = n
        b = 2 * n
        c = 3 * n
        if a ^ b == c:
            resultat += 1

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())