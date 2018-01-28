# -------------------------------------------------------------------------------
# Name:        pb135
# Purpose:     project euler
# Created:     27/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    sol = [0] * 1000001
    compteur = 0

    for u in range(1, 1000001):
        for v in range(1, (1000001 // u)+1):
            if (u+v) % 4 == 0 and 3 * v > u and (3*v-u) % 4 == 0:
                sol[u*v] += 1

    for k in sol:
        if k == 10:
            compteur += 1

    print(compteur)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())