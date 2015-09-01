# -------------------------------------------------------------------------------
# Name:        pb221
# Purpose:     project euler
# Created:     18/07/2015
# -------------------------------------------------------------------------------

import time
import sys


def div_inf_sqrt(n):          # renvoie les diviseurs de n^2 + 1 qui sont inférieus à sqrt(n^2+1)
    n1 = n**2 + 1
    t = []
    for i in range(1, n + 1):
        if n1 % i == 0:
            t.append(i)
    return t


def main():
    start = time.perf_counter()
    alexandrians = set()

    for k in range(1, 78000):
        for j in div_inf_sqrt(k):
            alexandrians.add(int(k*(k+j)*(k+(k**2+1)/j)))

    print(sorted(set(alexandrians))[149999])
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())