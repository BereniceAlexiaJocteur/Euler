import time
import sys
import math


class Problem():

    def __init__(self):
        self.n = 10
        self.k_origin = 1+2/math.sqrt(3)
        self.list_circles = [[(-1, None)], [(self.k_origin, ((0, 0), (1, 1), (1, 2))),
                            (self.k_origin, ((0, 0), (1, 0), (1, 2))), (self.k_origin, ((0, 0), (1, 0), (1, 1)))]]
        self.res = 1 - 3*(1/self.k_origin)**2

    def descartes(self, trip1, trip2, trip3):
        k1 = self.list_circles[trip1[0]][trip1[1]][0]
        k2 = self.list_circles[trip2[0]][trip2[1]][0]
        k3 = self.list_circles[trip3[0]][trip3[1]][0]
        k4 = k1 + k2 + k3 + 2*math.sqrt(k1*k2+k2*k3+k3*k1)
        self.res -= (1/k4)**2
        return k4, (trip1, trip2, trip3)

    def get_res(self):
        for k in range(2, self.n+2):
            self.list_circles.append([])
            visited = []
            for i in self.list_circles[k-1]:
                origin = (k-1, self.list_circles[k-1].index(i))
                if sorted([origin, i[1][0], i[1][1]]) not in visited:
                    self.list_circles[k].append(self.descartes(origin, i[1][0], i[1][1]))
                    visited.append(sorted([origin, i[1][0], i[1][1]]))
                if sorted([origin, i[1][1], i[1][2]]) not in visited:
                    self.list_circles[k].append(self.descartes(origin, i[1][1], i[1][2]))
                    visited.append(sorted([origin, i[1][1], i[1][2]]))
                if sorted([origin, i[1][0], i[1][2]]) not in visited:
                    self.list_circles[k].append(self.descartes(origin, i[1][0], i[1][2]))
                    visited.append(sorted([origin, i[1][0], i[1][2]]))

    def solve(self):
        self.get_res()
        print(round(self.res, 8))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())