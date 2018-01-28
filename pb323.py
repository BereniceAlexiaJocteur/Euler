from fractions import *


def solve(n):
        som = Fraction(0)
        for i in range(n):
            prob = Fraction(1) - (Fraction(1) - Fraction(1, 2**i))**32
            som += prob
        return round(float(som), 10)


print(solve(200))