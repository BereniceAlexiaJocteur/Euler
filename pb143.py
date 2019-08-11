import time
import sys
import math


class Problem():

    def __init__(self):
        self.bound = 120000
        self.doubles = []
        self.len_doubles = None
        self.index = dict()
        self.sums = []

    def generate_doubles(self): # génération triangles 120 degres
        for m in range(2, int(math.sqrt(self.bound)+1)):
            for n in range(1, m):
                if math.gcd(m, n) != 1 or (m - n) % 3 == 0:
                    continue
                p = 2*m*n+n**2
                q = m**2-n**2
                for k in range(1, self.bound//(p+q)+1):
                    self.doubles.append((k*p, k*q))
                    self.doubles.append((k*q, k*p))
        self.doubles.sort()
        self.len_doubles = len(self.doubles)

    def init_index(self):
        value = self.doubles[0][0]
        i = 0
        self.index[value] = i
        test = True
        while test:
            while self.doubles[i][0] == value:
                i += 1
                if i >= self.len_doubles:
                    test = False
                    break
            value = self.doubles[i][0]
            self.index[value] = i
            i += 1
            if i >= self.len_doubles:
                test = False
                break

    def get_sums(self):  # genere les groupes de 3 triangles avec 1 coté commun 2 a 2
        for i in self.doubles:
            first = i[0]
            second = i[1]
            v1 = []
            v2 = []
            for ind_j in range(self.index[first], len(self.doubles)):
                if self.doubles[ind_j][0] != first:
                    break
                v1.append(self.doubles[ind_j][1])
            for ind_k in range(self.index[second], len(self.doubles)):
                if self.doubles[ind_k][0] != second:
                    break
                v2.append(self.doubles[ind_k][1])
            v1 = set(v1)
            v2 = set(v2)
            inter = v1.intersection(v2)
            for v in inter:
                som = first + second + v
                if som <= self.bound and som not in self.sums:
                    self.sums.append(som)

    def solve(self):
        self.generate_doubles()
        self.init_index()
        self.get_sums()
        print(sum(self.sums))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())