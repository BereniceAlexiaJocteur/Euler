# -------------------------------------------------------------------------------
# Name:        pb148
# Purpose:     project euler
# Created:     26/08/2015
# -------------------------------------------------------------------------------

import time
import sys


def number_non_divisible_by_7_on_row(n):
    res = 1
    d = n
    while d > 0:
        d, r = divmod(d, 7)
        res *= r + 1
    return res


def main():
    start = time.perf_counter()
    somme = 0

    for i in range(10**9):
        somme += number_non_divisible_by_7_on_row(i)

    print(somme)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())