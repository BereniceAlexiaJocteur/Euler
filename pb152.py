import time
import sys
import math
import functools


class SparsePolynomialBounded():

    def __init__(self, bound):
        self.data = {}
        self.bound = bound

    def append(self, value):
        if value[0] <= self.bound:
            self.data[value[0]] = value[1]

    def __str__(self):
        s = ""
        for k in self.data.keys():
            s += str(self.data[k])+"x^"+str(k)+" + "
        s = s.replace("+ -", "- ")
        return s[:-2]

    def __mul__(self, other):
        p = SparsePolynomialBounded(self.bound)
        for coeff1 in self.data.keys():
            for coeff2 in other.data.keys():
                coeff = coeff1 + coeff2
                if coeff > self.bound:
                    break
                w = self.data[coeff1]*other.data[coeff2]
                if coeff in p.data:
                    p.data[coeff] += w
                else:
                    p.append((coeff, w))
        return p

    def get_coeff(self, n):
        if n in self.data:
            return self.data[n]
        else:
            return 0


class Problem():

    def __init__(self, n):
        self.n = n
        self.lcm_value = None
        self.terms = []
        self.res = None

    @staticmethod
    def lcm(numbers):
        return functools.reduce(lambda x, y: (x*y)//math.gcd(x, y), numbers, 1)

    def get_lcm_value(self):
        self.lcm_value = self.lcm(range(2, self.n+1))

    def init_terms(self):
        for i in range(2, self.n+1):
            self.terms.append(self.lcm_value//i**2)

    def get_res(self):
        p = SparsePolynomialBounded(self.lcm_value)
        p.append((0, 1))
        p.append((self.terms[0], 1))
        for i in range(1, len(self.terms)):
            print(i)
            pi = SparsePolynomialBounded(self.lcm_value)
            pi.append((0, 1))
            pi.append((self.terms[i], 1))
            p = p*pi
        self.res = p.get_coeff(self.lcm_value)

    def solve(self):
        self.get_lcm_value()
        self.init_terms()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(45)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())