# -------------------------------------------------------------------------------
# Name:        pb213
# Purpose:     project euler
# Created:     07/02/2015
# -------------------------------------------------------------------------------

import numpy
import fractions
import time
import sys


class Problem():

    def __init__(self):
        self.n = 30
        self.size = self.n**2
        self.number_iter = 50
        self.transition = numpy.zeros((self.size, self.size))

    def init_transition(self):
        for k in range(self.size):
            i = k // self.n
            j = k % self.n
            if i in range(1, self.n-1):
                if j in range(1, self.n-1):
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 4)
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 4)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 4)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 4)
                elif j == 0:
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 3)
                else:
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 3)
            elif i == 0:
                if j in range(1, self.n-1):
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 3)
                elif j == 0:
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 2)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 2)
                else:
                    self.transition[k][(i+1)*self.n+j] = fractions.Fraction(1, 2)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 2)
            else:
                if j in range(1, self.n-1):
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 3)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 3)
                elif j == 0:
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 2)
                    self.transition[k][i*self.n+(j+1)] = fractions.Fraction(1, 2)
                else:
                    self.transition[k][(i-1)*self.n+j] = fractions.Fraction(1, 2)
                    self.transition[k][i*self.n+(j-1)] = fractions.Fraction(1, 2)

    def solve(self):
        self.init_transition()
        mat = numpy.matrix(self.transition)**self.number_iter
        print(round(numpy.sum(numpy.prod(1-mat[:, p]) for p in range(self.size)), 6))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
