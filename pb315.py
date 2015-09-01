# -------------------------------------------------------------------------------
# Name:        pb315
# Purpose:     project euler
# Created:     06/07/2015
# -------------------------------------------------------------------------------

import time
import sympy
import sys


def sumdigits(n):
    r = 0
    while n:
        r, n = r + n % 10, n // 10
    return r


def sam(n, t):
    r = 0
    while n:
        r += t[n % 10]
        n //= 10
    return 2 * r


def maxim(a, b):
    y = int(a, 2) ^ int(b, 2)
    z = '{0:0{1}b}'.format(y, len(a))
    return sumdigits(int(z))


def trans(n, t):
    s = ""
    while n:
        d = n % 10
        n //= 10
        s = t[d] + s
    return s


def test(n, t1, t2):
    s = 0
    m = 0
    vide = "00000000"
    prec = vide
    while n > 9:
        s += sam(n, t1)
        m += maxim(prec, trans(n, t2))
        prec = trans(n, t2)
        n = sumdigits(n)
    m += maxim(prec, trans(n, t2)) + maxim(trans(n, t2), vide)
    s += sam(n, t1)
    return s - m


def main():
    start = time.perf_counter()
    tableauchiffres = [6, 2, 5, 5, 4, 5, 6, 4, 7, 6]
    tableaumax = ["01111101", "01010000", "00110111", "01010111", "01011010", "01001111", "01101111", "01011001",
                  "01111111", "01011111"]
    p = sympy.primerange(10 ** 7, 2 * 10 ** 7)
    resultat = 0

    for u in p:
        resultat += test(u, tableauchiffres, tableaumax)

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())