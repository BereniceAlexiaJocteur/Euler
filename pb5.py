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
        self.sieve = primes.primes(self.n)

    def get_smallest_multiple(self):
        smallest_number = 1
        for i in self.sieve:
            temp = i
            while temp <= self.n:
                temp *= i
            smallest_number *= temp // i
        return smallest_number

    def solve(self):
        self.init_sieve()
        print(self.get_smallest_multiple())


def main():
    start = time.perf_counter()
    u = Problem(20)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())