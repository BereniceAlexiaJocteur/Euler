# -------------------------------------------------------------------------------
# Name:        pb149
# Purpose:     project euler
# Created:     08/09/2015
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self):
        self.matrix = [[0 for x in range(2000)] for x in range(2000)]

    def init_matrix(self):
        for k in range(1, 56):
            self.matrix[(k - 1) // 2000][(k - 1) % 2000] = ((100003 - 200003 * k + 300007 * k ** 3) % 1000000) - 500000
        for k in range(56, 4000001):
            self.matrix[(k - 1) // 2000][(k - 1) % 2000] = ((self.matrix[(k - 25) // 2000][(k - 25) % 2000] +
                                                            self.matrix[(k - 56) // 2000][
                                                                (k - 56) % 2000] + 1000000) % 1000000) - 500000

    @staticmethod
    def get_max_sublist(l):
        best = 0
        cur_best = 0
        for i in l:
            cur_best = max(cur_best + i, 0)
            best = max(best, cur_best)
        return best

    def get_max_line(self):
        best = 0
        for i in range(2000):
            temp = self.get_max_sublist(self.matrix[i])
            if temp > best:
                best = temp
        return best

    def get_max_row(self):
        best = 0
        for i in range(2000):
            liste = (self.matrix[j][i] for j in range(2000))
            temp = self.get_max_sublist(liste)
            if temp > best:
                best = temp
        return best

    def get_max_diag(self):
        liste = (self.matrix[j][j] for j in range(0, 2000))
        best = self.get_max_sublist(liste)
        for i in range(1, 2000):
            liste1 = (self.matrix[j][j + i] for j in range(0, 2000 - i))
            liste2 = (self.matrix[j + i][j] for j in range(0, 2000 - i))
            temp1 = self.get_max_sublist(liste1)
            temp2 = self.get_max_sublist(liste2)
            temp = max(temp1, temp2)
            if temp > best:
                best = temp
        return best

    def get_max_antidiag(self):
        best = self.matrix[0][0]
        for i in range(1, 2000):
            liste1 = (self.matrix[i - j][j] for j in range(0, i + 1))
            liste2 = (self.matrix[2000 - 1 - j][i + j] for j in range(0, 2000 - i))
            temp1 = self.get_max_sublist(liste1)
            temp2 = self.get_max_sublist(liste2)
            temp = max(temp1, temp2)
            if temp > best:
                best = temp
        return best

    def solve(self):
        self.init_matrix()
        print(max(self.get_max_line(), self.get_max_row(), self.get_max_diag(), self.get_max_antidiag()))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
