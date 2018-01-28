# -------------------------------------------------------------------------------
# Name:        pb329
# Purpose:     project euler
# Created:     06/09/2015
# -------------------------------------------------------------------------------

import time
import sys
import primes
import fractions
import functools


class Problem():

    def __init__(self, n, seq):
        self.n = n
        self.seq = seq
        self.g_dic = {}
        self.sieve = primes.primes(self.n)

    def g(self, n, c):
        key_format = str(n) + ', ' + str(c)
        if key_format in self.g_dic:
            return self.g_dic[key_format]
        if n in self.sieve:
            if c == 'P':
                self.g_dic[key_format] = fractions.Fraction(2, 3)
                return self.g_dic[key_format]
            else:
                self.g_dic[key_format] = fractions.Fraction(1, 3)
                return self.g_dic[key_format]
        else:
            if c == 'P':
                self.g_dic[key_format] = fractions.Fraction(1, 3)
                return self.g_dic[key_format]
            else:
                self.g_dic[key_format] = fractions.Fraction(2, 3)
                return self.g_dic[key_format]

    @functools.lru_cache(maxsize=None)
    def get_probabilty(self, n, seq):
        if not seq:
            return fractions.Fraction(1)
        s0 = seq[0]
        if n == 1:
            return self.g(n, s0) * self.get_probabilty(2, seq[1:])
        elif n == self.n:
            return self.g(n, s0) * self.get_probabilty(self.n - 1, seq[1:])
        else:
            return fractions.Fraction(1, 2) * self.g(n, s0) * self.get_probabilty(n - 1, seq[1:]) + fractions.Fraction(
                1, 2) * self.g(n, s0) * self.get_probabilty(n + 1, seq[1:])

    def solve(self):
        resu = 0
        for i in range(1, self.n + 1):
            resu += self.get_probabilty(i, self.seq)
        print(resu * fractions.Fraction(1, self.n))


def main():
    start = time.perf_counter()
    u = Problem(500, 'PPPPNNPPPNPPNPN')
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
