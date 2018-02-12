# -------------------------------------------------------------------------------
# Name:        pb387
# Purpose:     project euler
# Created:     28/08/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


def sum_digits(n):
    s = 0
    while n > 0:
        s, n = s + n % 10, n // 10
    return s


def is_harshad(n):
    return n % sum_digits(n) == 0


def is_strong(n):
    return primes.is_prime_opti(n//sum_digits(n))


def gen_trunc_harshad(l1=list(range(1, 10)), lim=13, h=list(range(1, 10))):
    if lim == 1:
        return h
    l2 = []
    for i in l1:
        for j in range(10):
            temp = i*10+j
            if is_harshad(temp):
                l2.append(temp)
    h += l2
    return gen_trunc_harshad(l2, lim-1, h)


def main():
    start = time.perf_counter()
    ht = gen_trunc_harshad()
    somme = 0

    for u in ht:
        if is_strong(u):
            for k in [1, 3, 7, 9]:
                temp1 = u*10+k
                if primes.is_prime_opti(temp1):
                    somme += temp1

    print(somme)
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())