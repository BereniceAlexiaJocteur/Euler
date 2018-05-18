import time
import sys
import math
import functools


class Problem():

    def __init__(self, n):
        self.n = n
        self.number_odd_triplets = 0

    @staticmethod
    def binomial(n, k):
        if k > n or k < 0:
            return 0
        if k == 0 or n == k:
            return 1
        nt = 1
        for i in range(1, k + 1):
            nt = nt * (n - i + 1) // i
        return nt

    def brute_force_f(self, n, k):
        """we use f(n,k) = A159916(n,k) = binom(n,k) - A282011(n,k)"""
        res = self.binomial(n, k)
        for i in range((n+1)//4 + 1):
            terme = self.binomial(int(math.ceil(n/2)), 2*i)*self.binomial(n//2, k-2*i)
            res -= terme
        return res

    def brute_force(self):
        for i in range(1, self.n + 1, 2):
            for j in range(1, i + 1, 2):
                if self.brute_force_f(i, j) % 2 == 1:
                    self.number_odd_triplets += 1
                    print(i, j)

    """after bruteforcing we notice that the n,k that gives an odd triplet are such that n=1 mod 4 and for such a 
    given n the number of valid k is given by A001316. Thus if n1 is the i-th valid n then the number of valid k which 
    give a valid triplet is given by A001316(i).
    Finally I look up for the sequence of the partial sums of  A001316 it leads me to A006046 which has a nice recursive
    pattern : a(0) = 0, a(1) = 1, a(2k) = 3*a(k), a(2k+1) = 2*a(k) + a(k+1). Finally I need to compute 
    a((self.n-1)//4 + 1) """

    @functools.lru_cache(maxsize=None)
    def a(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n % 2 == 0:
            return 3 * self.a(n//2)
        else:
            u = n // 2
            return 2 * self.a(u) + self.a(u+1)

    def get(self):
        self.number_odd_triplets = self.a((self.n-1)//4 + 1)

    def solve(self):
        self.get()
        print(self.number_odd_triplets)


def main():
    start = time.perf_counter()
    u = Problem(10**12)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
