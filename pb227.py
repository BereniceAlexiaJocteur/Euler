# -------------------------------------------------------------------------------
# Name:        pb227
# Purpose:     project euler
# Created:     08/02/2016
# -------------------------------------------------------------------------------

import numpy
import fractions
import time
import sys


class Problem():

    def __init__(self):
        self.size = 50
        self.number_iter = 10**5
        self.transition = numpy.zeros((self.size+1, self.size+1))

    def init_transition(self):
        self.transition[0][0] = 1
        self.transition[1][0] = fractions.Fraction(2, 9)
        self.transition[1][1] = fractions.Fraction(1, 36) + fractions.Fraction(1, 2)
        self.transition[1][2] = fractions.Fraction(2, 9)
        self.transition[1][3] = fractions.Fraction(1, 36)
        for i in range(2, self.size-1):
            self.transition[i][i-2] = fractions.Fraction(1, 36)
            self.transition[i][i-1] = fractions.Fraction(2, 9)
            self.transition[i][i] = fractions.Fraction(1, 2)
            self.transition[i][i+1] = fractions.Fraction(2, 9)
            self.transition[i][i+2] = fractions.Fraction(1, 36)
        self.transition[49][47] = fractions.Fraction(1, 36)
        self.transition[49][48] = fractions.Fraction(2, 9)
        self.transition[49][49] = fractions.Fraction(1, 36) + fractions.Fraction(1, 2)
        self.transition[49][50] = fractions.Fraction(2, 9)
        self.transition[50][48] = fractions.Fraction(1, 18)
        self.transition[50][49] = fractions.Fraction(4, 9)
        self.transition[50][50] = fractions.Fraction(1, 2)

    def solve(self):
        self.init_transition()
        trans = numpy.mat(self.transition)
        x = numpy.zeros((1, self.size+1))
        x[0][50] = 1
        esp = 0
        for i in range(1, self.number_iter):
            item_prev = x.item(0, 0)
            x = x*trans
            esp += i*(x.item((0, 0))-item_prev)
        print(round(esp, 6))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
