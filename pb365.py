# -------------------------------------------------------------------------------
# Name:        pb365
# Purpose:     project euler
# Created:     21/07/2015
# -------------------------------------------------------------------------------

import primes
import functools
import eulerfun
import time
import sys


def chinese_remainder(n, a):
    sum = 0
    prod = functools.reduce(lambda u, v: u*v, n)

    for n_i, a_i in zip(n, a):
        pc = prod / n_i
        sum += a_i * mul_inv(pc, n_i) * pc
    return prod, int(sum % prod)


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def decimal_to_base(n, b):
    t = []
    d = n
    while d > 0:
        d, r = divmod(d, b)
        t.append(r)
    return t


def lucas(n, m, q):
    res = 1
    n2 = decimal_to_base(n, q)
    m2 = decimal_to_base(m, q)
    for k in range(len(n2)):
        if k > len(m2) - 1:
            temp = 0
        else:
            temp = m2[k]
        res = (res * eulerfun.binomial(n2[k], temp)) % q
    return res


def main():
    start = time.perf_counter()
    p = primes.primes(5000)
    i = 0
    resultat = 0

    while p[i] < 1000:
        i += 1

    p = p[i:len(p)]
    p1 = [0] * len(p)

    for j in range(len(p1)):
        p1[j] = lucas(10**18, 10**9, p[j])

    for a1 in range(len(p) - 2):
        pa = p[a1]
        pla = p1[a1]
        for b1 in range(a1 + 1, len(p) - 1):
            nc1 = [pa, p[b1]]
            ac1 = [pla, p1[b1]]
            nab, aab = chinese_remainder(nc1, ac1)
            for c1 in range(b1 + 1, len(p)):
                nc2 = [nab, p[c1]]
                ac2 = [aab, p1[c1]]
                resultat += chinese_remainder(nc2, ac2)[1]

    print(resultat-20)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())