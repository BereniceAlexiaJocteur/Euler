# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import primes
import itertools


class Problem():

    def __init__(self):
        self.digits = '1234567'
        self.candidates = []

    @staticmethod
    def format_perm(p):
        s = ''
        for i in p:
            s += i
        return s

    def init_candidates(self):
        for i in itertools.permutations(self.digits):
            self.candidates.append(int(self.format_perm(i)))
        self.candidates.sort(reverse=True)

    def get_largest(self):
        for i in self.candidates:
            if primes.is_prime_opti(int(i)):
                return i

    def solve(self):
        self.init_candidates()
        print(self.get_largest())


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())