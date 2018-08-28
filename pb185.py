import time
import sys
import numpy


class Problem():

    def __init__(self):
        self.list_test = [5616185650518293,
            3847439647293047,
            5855462940810587,
            9742855507068353,
            4296849643607543,
            3174248439465858,
            4513559094146117,
            7890971548908067,
            8157356344118483,
            2615250744386899,
            8690095851526254,
            6375711915077050,
            6913859173121360,
            6442889055042768,
            2321386104303845,
            2326509471271448,
            5251583379644322,
            1748270476758276,
            4895722652190306,
            3041631117224635,
            1841236454324589,
            2659862637316867]
        self.list_result_test = [2,
            1,
            3,
            3,
            3,
            1,
            2,
            3,
            1,
            2,
            3,
            1,
            1,
            2,
            0,
            2,
            2,
            3,
            1,
            3,
            3,
            2]
        self.matrix = []
        self.vector_result = []
        self.pre_treated_res = None
        self.res = 0

    def init_vector_result(self):
        self.vector_result = [1 for i in range(16)]
        self.vector_result += self.list_result_test
        self.vector_result = numpy.array(self.vector_result)

    def init_matrix(self):
        for i in range(16):
            u = [0]*160
            for j in range(i*10, i*10+10):
                u[j] = 1
            self.matrix.append(u)
        for i in self.list_test:
            u = [0]*160
            s = str(i)
            for j in range(len(s)):
                digit = int(s[j])
                u[j * 10 + digit] = 1
            self.matrix.append(u)
        self.matrix = numpy.array(self.matrix)

    def solve(self):
        self.init_vector_result()
        self.init_matrix()
        self.pre_treated_res = numpy.linalg.lstsq(self.matrix, self.vector_result, rcond=None)
        print(self.pre_treated_res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
