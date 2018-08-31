import time
import sys
import sympy


class Problem():

    def __init__(self):
        self.n = 10**15
        self.mod = sympy.factorial(15)
        self.res = 0

    def mult_matrix(self, matrix1, matrix2):  # multiplier deux matrices le tout modulo self.mod
        len_i = len(matrix1)
        len_j = len(matrix2[0])
        len_k = len(matrix2)
        matrix_res = [[0 for j in range(len_j)]for i in range(len_i)]
        for i in range(len_i):
            for j in range(len_j):
                temp_sum = 0
                for k in range(len_k):
                    temp_sum = (temp_sum + matrix1[i][k]*matrix2[k][j]) % self.mod
                matrix_res[i][j] = temp_sum
        return matrix_res

    def exponentitaion_by_squaring_matrix(self, matrix, power):  # eleve matrix a la puissance power le tout modulo mod
        if power == 1:
            return matrix
        if power % 2 == 0:
            return self.exponentitaion_by_squaring_matrix(self.mult_matrix(matrix, matrix), power//2)
        else:
            return self.mult_matrix(matrix, self.exponentitaion_by_squaring_matrix(self.mult_matrix(matrix, matrix),
                                                                                   (power-1)//2))

    def Fn(self, x):
        matrix_A = [[0, x**2, 0], [1, x, 1], [0, 0, 1]]
        matrix_line = [[x, x**2, x]]
        return self.mult_matrix(matrix_line, self.exponentitaion_by_squaring_matrix(matrix_A, self.n-1))[0][2]

    def get_res(self):
        for i in range(101):
            self.res = (self.res + self.Fn(i)) % self.mod

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())