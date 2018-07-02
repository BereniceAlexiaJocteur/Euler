import time
import sys
import primes
import math


class Problem():

    def __init__(self, n, d):
        self.n = n
        self.d = d
        self.list_primes = primes.sieve8(int(math.sqrt(n))+1)  # list of primes p such that p**2 <= n
        self.list_primes_candidates = []  # list of tuples (p, i) such that d divides sigma(p^i)
        self.res = 0  # compte les multiples des premiers qui conviennent puis enleve les doublons

    def init_list_candidates(self):
        candidate = self.d-1
        while candidate < self.n:  # determines the primes such that d divides them
            if primes.is_prime_opti(candidate):
                self.list_primes_candidates.append((candidate, candidate, 1))
            candidate += self.d
        for p in self.list_primes:
            candidate = p**2
            exponent = 2
            while candidate < self.n:
                sigma = (candidate*p - 1)//(p - 1)
                if sigma % self.d == 0:
                    self.list_primes_candidates.append((p**exponent, p, exponent))
                candidate *= p
                exponent += 1
        self.list_primes_candidates = sorted(self.list_primes_candidates)

    def count(self):
        for i in self.list_primes_candidates:  # compte les multiples de p^i qui ne sont pas mutiples de p^(i+1)
            compteur = self.n // i[0]
            self.res = self.res + (i[0]*(compteur*(compteur+1))//2)
            compteur = self.n // (i[1]**(i[2]+1))
            self.res = self.res - (i[1] ** (i[2]+1) * (compteur * (compteur + 1)) // 2)
        for i in range(len(self.list_primes_candidates)):  # on enleve les doublons quand deux premiers différents sont
            #  multpliés
            nombre = self.list_primes_candidates[i][0]
            if nombre**2 > self.n:
                break
            for j in range(i+1, len(self.list_primes_candidates)):
                produit = nombre * self.list_primes_candidates[j][0]
                if produit > self.n:
                    break
                compteur = self.n // produit
                self.res = self.res - (produit*(compteur*(compteur+1))//2)

    def solve(self):
        self.init_list_candidates()
        self.count()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(10**11, 2017)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())