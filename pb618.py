import time
import sys
import primes
import functools


class Problem():  # recursion too deep

    def __init__(self, n):
        self.limit = n
        self.current_fib = 5  # nombre de Fibonacci actuel
        self.previous_fib = 3
        self.prime_list = []
        self.res = 5

    @functools.lru_cache(maxsize=None)
    def function(self, n, current_product, index_current_prime):
        if n == 0:
            return current_product
        elif n < self.prime_list[index_current_prime]:
            return 0
        elif index_current_prime == 0:
            return self.function(n - self.prime_list[index_current_prime],
                          current_product * self.prime_list[index_current_prime], index_current_prime)
        else:
            return self.function(n, current_product, index_current_prime-1) + \
                   self.function(n - self.prime_list[index_current_prime],
                                 current_product*self.prime_list[index_current_prime], index_current_prime)

    def get(self):
        for i in range(5, self.limit+1):
            print(i)
            self.prime_list = primes.sieve(self.current_fib)
            self.res += self.function(self.current_fib, 1, len(self.prime_list)-1)
            self.previous_fib, self.current_fib = self.current_fib, self.previous_fib+self.current_fib

    def solve(self):
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(24)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())