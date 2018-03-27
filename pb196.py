from sympy import sieve
import time
import sys
import numpy


class Problem():

    def __init__(self):
        self.n1 = 5678027
        self.n2 = 7208785
        self.primes = None
        self.triangle = None

    @staticmethod
    def triangular_number(n):
        return ((n+1)*n)//2

    def init_primes(self, n):
        self.primes = sieve.primerange(self.triangular_number(n-3)+1, self.triangular_number(n+2)+100)

    def init_triangle(self, n):
        array1 = numpy.empty(n-2, dtype='bool_')
        tri = self.triangular_number(n - 3) + 1
        j = next(self.primes)
        for i in range(n-2):
            if tri+i == j:
                array1[i] = True
                j = next(self.primes)
            else:
                array1[i] = False
        array2 = numpy.empty(n-1, dtype='bool_')
        tri = self.triangular_number(n - 2) + 1
        for i in range(n-1):
            if tri+i == j:
                array2[i] = True
                j = next(self.primes)
            else:
                array2[i] = False
        array3 = numpy.empty(n, dtype='bool_')
        tri = self.triangular_number(n - 1) + 1
        for i in range(n):
            if tri+i == j:
                array3[i] = True
                j = next(self.primes)
            else:
                array3[i] = False
        array4 = numpy.empty(n+1, dtype='bool_')
        tri = self.triangular_number(n) + 1
        for i in range(0, n+1):
            if tri+i == j:
                array4[i] = True
                j = next(self.primes)
            else:
                array4[i] = False
        array5 = numpy.empty(n+2, dtype='bool_')
        tri = self.triangular_number(n+1) + 1
        for i in range(n+2):
            if tri+i == j:
                array5[i] = True
                j = next(self.primes)
            else:
                array5[i] = False
        self.triangle = numpy.asarray((array1, array2, array3, array4, array5))

    def solve(self):
        self.init_primes(10**6)
        self.init_triangle(10**6)
        print(self.triangle)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())