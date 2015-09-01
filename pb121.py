# -------------------------------------------------------------------------------
# Name:        pb121
# Purpose:     project euler
# Created:     26/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def main():
    start = time.perf_counter()
    t1 = [1, 1]
    lim = 16
    cas_fav = 0

    for i in range(2, lim):
        t2 = [1] * (i+1)
        for j in range(1, i):
            t2[j] = i * t1[j-1] + t1[j]
        t2[i] = i * t1[-1]
        t1 = t2[:]

    cas_tot = 16 * t1[-1]

    for k in range(8):
        cas_fav += t1[k]

    print(cas_tot // cas_fav)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())