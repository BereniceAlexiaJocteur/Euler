import time
import sys


class Problem():

    def __init__(self):
        self.curr_max = 10400
        self.curr_binomial_coefficient = 2600
        self.curr_power = 8

    def get_max(self):
        for i in range(4, 27):
            self.curr_power *= 2
            self.curr_binomial_coefficient = self.curr_binomial_coefficient*(26-i+1)//i
            p = (self.curr_power-i-1)*self.curr_binomial_coefficient
            if p > self.curr_max:
                self.curr_max = p


    def solve(self):
        self.get_max()
        print(self.curr_max)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())