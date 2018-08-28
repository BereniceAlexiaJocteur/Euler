import time
import sys
import sympy
import math
import primes
import functools
import itertools


class Problem():

    def __init__(self):
        self.factorial = math.factorial(13)
        self.list_prime_candidates = []  # list of prime p such that p-1 divides factorial and we give their max factor
        self.list_product = []
        self.list_prime_valuation_one = []
        self.list_valid_n = []  # list of n such that phi(n) = factorial
        self.length = None

    def get_list_prime_candidates(self):
        for d in sympy.divisors(self.factorial):
            p = d+1
            if primes.is_prime_opti(p):
                n = self.factorial // d
                exp = 0
                while n % p == 0:
                    n = n // p
                    exp += 1
                self.list_prime_candidates.append((p, exp))
        self.list_prime_candidates.sort()

    @staticmethod
    def prod_pair(iterable):
        return functools.reduce(lambda x, y: (x[0]*y[0], x[1]*y[1]), iterable)

    def init_list_product(self):
        liste_primes = []
        for i in self.list_prime_candidates:
            if i[1] != 0:
                n = i[0]
                phi = i[0] - 1
                l = [(1, 1), (n, phi)]
                for j in range(i[1]):
                    n *= i[0]
                    phi *= i[0]
                    l.append((n, phi))
                liste_primes.append(l)
            else:
                self.list_prime_valuation_one.append((i[0], i[0]-1))
        self.list_product = list(map(self.prod_pair, itertools.product(*iter(liste_primes))))
        self.length = len(self.list_prime_valuation_one)

    def f(self, number, phi, index):
        if phi == self.factorial:
            self.list_valid_n.append(number)
        elif phi*self.list_prime_valuation_one[index][1] <= self.factorial:
            if index < self.length-1:
                self.f(number, phi, index+1)
                self.f(number*self.list_prime_valuation_one[index][0], phi*self.list_prime_valuation_one[index][1],
                       index+1)
            elif index == self.length-1:
                if phi*self.list_prime_valuation_one[index][1] == self.factorial:
                    self.list_valid_n.append(number*self.list_prime_valuation_one[index][0])

    def fill_list_possible_n(self):
        for i in self.list_product:
            self.f(i[0], i[1], 0)
        self.list_valid_n = list(set(self.list_valid_n))
        self.list_valid_n.sort()

    def solve(self):
        self.get_list_prime_candidates()
        self.init_list_product()
        self.fill_list_possible_n()
        print(self.list_valid_n[149999])


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
