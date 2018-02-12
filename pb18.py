# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self):
        self.matrix = None
        self.l = 0

    def init_matrix(self):
        with open("p18_pyramid.txt") as f:
            self.matrix = f.readlines()
        self.matrix = [x.strip('\n') for x in self.matrix]
        self.matrix = [x.split(',') for x in self.matrix]
        self.matrix = [j.split() for i in self.matrix for j in i]
        self.l = len(self.matrix)
        for i in range(self.l):
            for j in range(i+1):
                self.matrix[i][j] = int(self.matrix[i][j])

    def get_max_sum(self):
        for i in range(self.l-2, -1, -1):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] += max(self.matrix[i+1][j], self.matrix[i+1][j+1])
        return self.matrix[0][0]

    def solve(self):
        self.init_matrix()
        print(self.get_max_sum())


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())