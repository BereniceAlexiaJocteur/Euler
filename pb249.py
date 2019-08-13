import time
import sys
import collections
import primes


class Problem():

    def __init__(self):
        self.dico = {0: 1}
        self.primes_list = None
        self.res = 0

    def init_primes(self):
        self.primes_list = primes.sieve(5000)

    def init_dico(self):
        for p in self.primes_list:
            dico_temp = dict()
            for i in self.dico:
                dico_temp[p+i] = self.dico[i]
            self.dico = dict(collections.Counter(self.dico)+collections.Counter(dico_temp))

    def get_res(self):
        for i in self.dico:
            if primes.is_prime_opti(i):
                self.res = self.res + self.dico[i]
                if self.res > 10**16:
                    self.res = self.res % 10**16

    def solve(self):
        self.init_primes()
        self.init_dico()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())