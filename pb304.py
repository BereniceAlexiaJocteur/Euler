import time
import sys
import primes
import functools


class Problem():

    def __init__(self, limit, mod):
        self.limit = limit
        self.mod = mod
        self.res = 0

    @functools.lru_cache(maxsize=None)
    def fibonacci(self, n):
        ''''Calculating Fibonacci Numbers by Fast Doubling
        https://chunminchang.github.io/blog/post/calculating-fibonacci-numbers-by-fast-doubling'''
        q, r = divmod(n, 2)
        if r == 0:
            return ((2*self.fibonacci(q-1)+self.fibonacci(q))*self.fibonacci(q)) % self.mod
        else:
            return (pow(self.fibonacci(q+1), 2, self.mod) + pow(self.fibonacci(q), 2, self.mod)) % self.mod

    '''The recursive version was too deep so I used an iterative solution equivalent to the recursive one'''

    def fibonacci_mod(self, n):
        a, b = 0, 1
        binary = bin(n)[2:]
        for bit in binary:
            a, b = a * (b * 2 - a), a * a + b * b
            if bit == "1":
                a, b = b, a + b
            a %= self.mod
            b %= self.mod
        return a

    def get(self):
        k = 10**14
        for i in range(1, self.limit+1):
            while not primes.is_prime_opti(k): # it uses Miller6rabin algorithm to test primality
                k += 1
            self.res = (self.res + self.fibonacci_mod(k)) % self.mod
        k += 1

    def solve(self):
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(10**5, 1234567891011)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
