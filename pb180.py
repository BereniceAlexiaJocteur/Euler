import fractions
import time
import sys


class Problem():

    def __init__(self, order):
        self.order = order
        self.set_of_rationals = set()
        self.set_of_sums = set()
        self.res = 0

    def init_set_of_rationnals(self):
        for i in range(2, self.order+1):
            for j in range(1, i):
                self.set_of_rationals.add(fractions.Fraction(j, i))

    def init_set_of_sums(self):
        list_of_rationals = list(self.set_of_rationals)
        for indice_x in range(len(list_of_rationals)):
            ax = list_of_rationals[indice_x].numerator
            bx = list_of_rationals[indice_x].denominator
            for indice_y in range(indice_x, len(list_of_rationals)):
                ay = list_of_rationals[indice_y].numerator
                by = list_of_rationals[indice_y].denominator
                for indice_z in range(len(list_of_rationals)):
                    az = list_of_rationals[indice_z].numerator
                    bz = list_of_rationals[indice_z].denominator
                    num1 = ax*by*bz
                    num2 = ay*bx*bz
                    num3 = az*bx*by
                    denom1 = bx*ay*az
                    denom2 = by*ax*az
                    denom3 = ax*ay*bz
                    if num1 + num2 == num3 or num1**2 + num2**2 == num3**2 or denom1 + denom2 == denom3 or denom1**2 + denom2**2 == denom3**2:
                        self.set_of_sums.add(list_of_rationals[indice_x] + list_of_rationals[indice_y] + list_of_rationals[indice_z])

    def get_res(self):
        somme = sum(self.set_of_sums)
        self.res = somme.numerator + somme.denominator

    def solve(self):
        self.init_set_of_rationnals()
        self.init_set_of_sums()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(35)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
