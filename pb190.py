# -------------------------------------------------------------------------------
# Name:        pb190
# Purpose:     project euler
# Created:     21/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def pmax(m):
    res = (2/(m+1))**(m*(m+1)/2)
    for i in range(2, m+1):
        res *= i**i
    return int(res)


def main():
    start = time.perf_counter()
    somme = 0

    for j in range(2, 16):
        somme += pmax(j)

    print(somme)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())