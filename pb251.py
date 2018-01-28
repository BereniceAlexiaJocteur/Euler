# -------------------------------------------------------------------------------
# Name:        pb251
# Purpose:     project euler
# Created:     29/08/2015
# -------------------------------------------------------------------------------

import sympy
import time
import functools
import sys


def factor_special(n):
    dic1 = sympy.factorint(n)
    dic2 = {}
    for i in dic1:
        if dic1[i] != 1:
            dic2[i] = dic1[i]//2
    return dic2


def getb(fac1, fac2):
    if not fac1 and not fac2:
        yield 1
        return
    for i in fac2:
        if i not in fac1:
            fac1[i] = 0
        fac1[i] += fac2[i]
    fac3 = sorted(fac1.items())
    nfactors = len(fac3)
    f = [0] * nfactors
    while True:
        yield functools.reduce(lambda x, y: x*y, [fac3[x][0]**f[x] for x in range(nfactors)], 1)
        i = 0
        while True:
            f[i] += 1
            if f[i] <= fac3[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                return


def main():
    start = time.perf_counter()
    lim = 10000000
    compteur = 0

    for k in range(int((lim+2)/6.779763)):
        a = 3*k+2
        num = (8*k+5)*(k+1)**2
        factor1 = factor_special(8*k+5)
        factor2 = sympy.factorint(k+1)
        gb = getb(factor1, factor2)
        for b in gb:
            c = num // b**2
            if a+b+c < lim:
                compteur += 1
                print(compteur, a)

    print(compteur)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())