import time
import sys
import math
from sympy import sieve


class Problem():

    def __init__(self):
        self.primes = None

    def r2(self, n):
        produit = 1
        while n % 2 == 0:
            n //= 2
        for p in self.primes:
            if n == 0:
                break
            expo = 0  # exposant du facteur premier
            while n % p == 0:
                n //= p
                expo += 1
            if p % 4 == 3 and expo % 2 == 1:
                return 0
            elif p % 4 == 1:
                produit *= (expo + 1)
        return produit

    def r3_naif(self, n):
        somme = 0
        for i in range(1, int(math.sqrt(n))+1):
            somme += self.r2(n-i**2)
        return somme

    def r3(self, n):
        initial_n = n
        lamb = 0
        while n % 9 == 0:
            n //= 9
            lamb += 1
        print(n)
        self.primes = sieve.primerange(3, n)
        if n % 24 == 11:
            return (3**lamb) * self.r3_naif(n)
        elif n % 24 == 19:
            return (2*3**lamb-1)*self.r3_naif(n)
        elif n % 72 == 3 or n % 72 == 51:
            return ((3**(lamb+1)-1)*self.r3_naif(n))//2
        else:
            return self.r3_naif(initial_n)

    def g(self, n):
        return self.r3(8*n+3)

    def solve(self):
        print(self.g(17526*10**9))



def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())