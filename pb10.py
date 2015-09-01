# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import primes


class Problem():

    def __init__(self, n):
        self.n = n
        self.sieve = []

    def init_sieve(self):
        self.sieve = primes.sieve8(self.n)

    def get_sum(self):
        somme = 0
        for i in self.sieve:
            somme += i
        return somme

    def solve(self):
        self.init_sieve()
        print(self.get_sum())


def main():
    start = time.perf_counter()
    u = Problem(2*10**6)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())