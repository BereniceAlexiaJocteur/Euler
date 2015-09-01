# -------------------------------------------------------------------------------
# Name:        pb429
# Purpose:     project euler
# Created:     27/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys

# S(p1^a1 p2^a2 .... pk^ak)= (1 + p1^(2*a1))(1 + p2^2*a2)....
# to get the ai of n! we use legendre's theorem


def padic_order(n, p):
    res = 0
    i = 1
    temp = n // p
    while temp > 0:
        res += temp
        i += 1
        temp = n // p**i
    return res


def main():
    start = time.perf_counter()
    pri = primes.primes(10**8)
    a = []
    resultat = 1

    for k in pri:
        a.append((k, padic_order(10**8, k)))
    del pri

    for k in a:
        terme = 1 + pow(k[0], 2*k[1], 1000000009)
        resultat = (resultat * terme) % 1000000009

    print(resultat)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())