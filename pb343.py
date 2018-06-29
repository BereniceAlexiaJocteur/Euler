import primes
import time
import sys


class NumberTheory():

    def __init__(self):
        self.primes_table = primes.sieve8(10**9)

    def is_prime(self, n):
        if n < 10**9:
            return n in self.primes_table
        else:
            return primes.is_prime_opti(n)

    def largest_divisor(self, n):  # returns the largest strist divisor of n if n is not prime otherwise returns n
        for i in self.primes_table:
            if n % i == 0:
                return n//i
            if n < i**2:
                return n


class Problem():

    def __init__(self):
        self.res = 0
        self.limit = 2*10**6
        self.numtheory = NumberTheory()

    def f(self, n):
        tot = 1+n
        if tot == 4 or tot == 2:
            return 1
        else:
            u = self.numtheory.largest_divisor(tot)
            if u == tot:  # if tot is prime f(tot - 1) = tot-1
                return tot-1
            else:  # else f(tot - 1) = f(u - 1)
                return self.f(u-1)

    def get_res(self):
        for k in range(1, self.limit+1):
            if k % 1000 == 0:
                print(k)
            self.res += self.f(k**3)

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())