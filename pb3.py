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
        self.lim = n
        self.sieve = []

    def init_sieve(self):
        self.sieve = primes.primes(10**4)

    def get_largest_prime_factor(self, n):
        largest_factor = 1
        for i in self.sieve:
            if n % i == 0:
                n //= i
                largest_factor = i
                while n % i == 0:
                    n //= i
            if n == 1:
                break
        return largest_factor

    def solve(self):
        self.init_sieve()
        print(self.get_largest_prime_factor(self.lim))


def main():
    start = time.perf_counter()
    u = Problem(600851475143)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())