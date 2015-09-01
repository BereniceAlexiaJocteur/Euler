# -------------------------------------------------------------------------------
# Name:        pb192
# Purpose:     project euler
# Created:     23/07/2015
# -------------------------------------------------------------------------------

import math
import time
import sys


def frac_cont_of_sqrt(n):
    """ return the continue fraction of sqrt(n)"""
    m0 = 0
    d0 = 1
    a0 = int(math.sqrt(n))
    mn = m0
    dn = d0
    an = a0
    t = [a0]
    while an != 2 * a0:
        mn = dn * an - mn
        dn = (n - mn**2) / dn
        an = int((a0 + mn) / dn)
        t.append(an)
    i = len(t)
    l = len(t) - 1
    while i < 128:
        t.append(t[1 + (i-1) % l])
        i += 1
    return t


def allow_half(t, k):
    """ check for the even case for semi convergents"""
    i = k
    s = 1
    while i > 0:
        diff = s*(t[i] - t[2*k-i])
        if diff > 0:
            return True
        if diff < 0:
            return False
        s *= -1
        i -= 1
    return ((k-1) & 1) != 0


def lowest_denominator(t, limit):
    n2 = 1
    d2 = 0
    n1 = t[0]
    d1 = 1
    i = 1
    while True:
        n = 0
        d = 0
        minval = (t[i]+1) // 2
        if (t[i] & 1) == 0 and not(allow_half(t, i)):
            minval += 1
        for q in range(minval, t[i] + 1):
            n = n2 + q * n1
            d = d2 + q * d1
            if d > limit:
                if q > minval:
                    return d2 + (q-1) * d1
                else:
                    return d1
        n2 = d2
        d2 = d1
        n1 = n
        d1 = d
        i += 1


def main():
    start = time.perf_counter()
    resultat = 0

    for u in range(1, 100001):
        if math.sqrt(u) != int(math.sqrt(u)):
            resultat += lowest_denominator(frac_cont_of_sqrt(u), 10**12)

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())