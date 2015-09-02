# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():
    def __init__(self, n):
        self.n = n
        self.matrix = None
        self.l = 0

    def init_matrix(self):
        with open("p11_grid.txt") as f:
            self.matrix = f.readlines()
        self.matrix = [x.strip('\n') for x in self.matrix]
        self.matrix = [x.split(',') for x in self.matrix]
        self.matrix = [j.split() for i in self.matrix for j in i]
        self.l = len(self.matrix)
        for i in range(self.l):
            for j in range(self.l):
                self.matrix[i][j] = int(self.matrix[i][j])

    def get_max_prod_line(self):
        max_prod = 0
        for i in range(self.l):
            for j in range(self.l - self.n + 1):
                temp = 1
                for k in range(self.n):
                    temp *= self.matrix[i][j + k]
                if temp > max_prod:
                    max_prod = temp
        return max_prod

    def get_max_prod_row(self):
        max_prod = 0
        for i in range(self.l - self.n + 1):
            for j in range(self.l):
                temp = 1
                for k in range(self.n):
                    temp *= self.matrix[i + k][j]
                if temp > max_prod:
                    max_prod = temp
        return max_prod

    def get_max_prod_diag(self):
        max_prod = 0
        for i in range(self.l - self.n + 1):
            for j in range(self.l - self.n + 1):
                temp = 1
                for k in range(self.n):
                    temp *= self.matrix[i + k][j + k]
                if temp > max_prod:
                    max_prod = temp
        return max_prod

    def get_max_prod_antidiag(self):
        max_prod = 0
        for i in range(self.l - self.n + 1):
            for j in range(self.n - 1, self.l):
                temp = 1
                for k in range(self.n):
                    temp *= self.matrix[i + k][j - k]
                if temp > max_prod:
                    max_prod = temp
        return max_prod

    def solve(self):
        self.init_matrix()
        print(max(self.get_max_prod_line(), self.get_max_prod_row(), self.get_max_prod_diag(),
                  self.get_max_prod_antidiag()))


def main():
    start = time.perf_counter()
    u = Problem(4)
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
