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
        n = primes.upper_bound_prime(self.n)
        self.sieve = primes.sieve8(n)

    def solve(self):
        self.init_sieve()
        print(self.sieve[self.n-1])


def main():
    start = time.perf_counter()
    u = Problem(10001)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())