# -------------------------------------------------------------------------------
# Name:        pb381
# Purpose:     project euler
# Created:     19/09/2015
# -------------------------------------------------------------------------------

import primes
import time
import sys


class Problem():

    def __init__(self, n):
        self.lim = n
        self.p = primes.primes(self.lim)[2:]
        self.somme = 0

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    def fonction(self, n):
        res = -1
        temp = n-1
        temp1 = temp
        for j in range(2, 5):
            res -= self.modinv(temp, n)
            temp1 = n - j
            temp *= temp1
        res -= self.modinv(temp, n)
        return res % n

    def getsum(self):
        for pri in self.p:
            self.somme += self.fonction(pri)

    def solve(self):
        self.getsum()
        print(self.somme)


def main():
    start = time.perf_counter()
    u = Problem(10**8)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())