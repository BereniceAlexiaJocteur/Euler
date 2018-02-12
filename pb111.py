# -------------------------------------------------------------------------------
# Name:        pb111
# Purpose:     project euler
# Created:     31/08/2015
# -------------------------------------------------------------------------------

import itertools
import primes
import time
import sys


class Problem():

    def __init__(self, n):
        self.digits = '0123456789'
        self.n = n

    @staticmethod
    def format_perm(t):
        s1 = ''
        for i in t:
            s1 += i
        return s1

    @staticmethod
    def get_rep_digit(d, n):  # return the string 'dd...dd' with n d
        s2 = ''
        dig = str(d)
        for i in range(n):
            s2 += dig
        return s2

    def s(self, n, d):
        lim = n-1
        i = lim
        somme = 0
        digits_available = self.digits.replace(str(d), '')
        while not somme:
            s_rep = ''
            for j in range(i):
                s_rep += str(d)
            for j in itertools.combinations_with_replacement(digits_available, n-i):
                js = self.format_perm(j)
                number = js + s_rep
                for k in set(itertools.permutations(number)):
                    ks = self.format_perm(k)
                    if ks[0] != '0' and primes.is_prime_opti(int(ks)):
                        somme += int(ks)
            i -= 1
        return somme

    def get_somme(self):
        somme = 0
        for i in range(10):
            somme += self.s(self.n, i)
        return somme

    def solve(self):
        print(self.get_somme())


def main():
    start = time.perf_counter()
    u = Problem(10)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())