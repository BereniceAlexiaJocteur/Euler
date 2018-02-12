# -------------------------------------------------------------------------------
# Name:        pb112
# Purpose:     project euler
# Created:     15/02/2015
# -------------------------------------------------------------------------------

import math
import time
import sys


def isdec(n):
    taille = int(math.log10(n)) + 1
    lastdig = n % 10
    temp = n
    for i in range(taille - 1):
        temp /= 10
        if temp % 10 < lastdig:
            return False
        else:
            lastdig = temp % 10
    return True


def isinc(n):
    taille = int(math.log10(n)) + 1
    lastdig = n % 10
    temp = n
    for i in range(taille - 1):
        temp /= 10
        if temp % 10 > lastdig:
            return False
        else:
            lastdig = temp % 10
    return True


def isbouncy(n):
    return not isdec(n) and not isinc(n)


def main():
    start = time.perf_counter()
    test = 0
    j = 99

    while 100 * test < 99 * j:
        j += 1
        if isbouncy(j):
            test += 1

    print(j)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())