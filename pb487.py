# -------------------------------------------------------------------------------
# Name:        pb487
# Purpose:     project euler
# Created:     14/04/2018
# -------------------------------------------------------------------------------

import time
import sys
import eulerfun
import primes


class Problem():

    def __init__(self):
        self.n = 10**12
        self.k = 10000
        self.k_initial = 10000
        self.list_bernoulli = None
        self.list_binomial_for_bernouilli = None
        self.list_binomial_for_sum = None
        self.res = 0
        self.mod = None

    def egcd(self, a, b):
        if a == 0:
            return b, 0, 1
        else:
            g, y, x = self.egcd(b % a, a)
            return g, x - (b // a) * y, y

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('modular inverse does not exist')
        else:
            return x % m

    @staticmethod
    def decimal_to_base(n, b):
        t = []
        d = n
        while d > 0:
            d, r = divmod(d, b)
            t.append(r)
        return t

    def lucas(self, n, m, q):
        res = 1
        n2 = self.decimal_to_base(n, q)
        m2 = self.decimal_to_base(m, q)
        for k in range(len(n2)):
            if k > len(m2) - 1:
                temp = 0
            else:
                temp = m2[k]
            res = (res * eulerfun.binomial(n2[k], temp)) % q
        return res

    def get_binomial_for_sum(self):  # penser au modulo avec Lucas
        self.list_binomial_for_sum = []
        for i in range(self.k + 1):
            self.list_binomial_for_sum.append(self.lucas(self.k+1, i, self.mod))

    def get_bernouilli(self):
        self.list_bernoulli = [1]
        self.list_binomial_for_bernouilli = [1, 1]
        for i in range(1, self.k+1):
            new_list_binomial_for_bernouilli = [1]
            for j in range(len(self.list_binomial_for_bernouilli)-1):
                new_list_binomial_for_bernouilli.append((self.list_binomial_for_bernouilli[j]+self.list_binomial_for_bernouilli[j+1])%self.mod)
            new_list_binomial_for_bernouilli.append(1)
            self.list_binomial_for_bernouilli = new_list_binomial_for_bernouilli
            bernoulli_number = 0
            for j in range(len(self.list_binomial_for_bernouilli)-2):
                bernoulli_number += (self.list_binomial_for_bernouilli[j] * self.list_bernoulli[j]) % self.mod
            bernoulli_number = (bernoulli_number * self.modinv(len(self.list_binomial_for_bernouilli)-1, self.mod)) % self.mod
            bernoulli_number = (-bernoulli_number) % self.mod
            self.list_bernoulli.append(bernoulli_number)

    def f(self, k): #  get binomials and get bernoulli a l'interieur + cpmmencer par la fin pour incrémenter la puissance de n dans le bon sens
        self.k = k
        self.get_binomial_for_sum()
        self.get_bernouilli()
        res = 0
        current_n = 1
        n_moded = (self.n+1) % self.mod
        for i in range(self.k, -1, -1):
            current_n = (current_n * n_moded) % self.mod
            res = (res + self.list_binomial_for_sum[i]*self.list_bernoulli[i]*current_n) % self.mod
        res = (res * self.modinv(self.k + 1, self.mod)) % self.mod
        return res

    def S(self):
        return ((self.n + 1) * self.f(self.k_initial) - self.f(self.k_initial + 1)) % self.mod

    def get_res(self):
        for i in range(2*10**9, 2*10**9+2000+1):
            if primes.is_prime_opti(i):
                print(i)
                self.mod = i
                self.res += self.S()

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
