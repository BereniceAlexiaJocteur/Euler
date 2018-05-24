import time
import sys


class LaggedFibonnaciGenerator():

    def __init__(self):
        self.list_of_sk = [0] * 55
        self.k = 1

    def next(self):
        if self.k <= 55:
            sk = (100003 - 200003*self.k + 300007*self.k**3) % 10**6
            self.k += 1
        else:
            sk = (self.list_of_sk[0] + self.list_of_sk[31]) % 10**6
        del self.list_of_sk[0]
        self.list_of_sk.append(sk)
        return sk


'''I used the algorithm presented here : https://en.wikipedia.org/wiki/Disjoint-set_data_structure'''


class UnionFind():

    def __init__(self):
        self.nodes = [UnionFind.Node() for _ in range(10**6)]

    def _find(self, i):
        return self.nodes[i].find()

    def union(self, i, j):
        iroot = self._find(i)
        jroot = self._find(j)
        if iroot == jroot:
            return
        if iroot.rank == jroot.rank:
            iroot.rank = iroot.rank + 1
        elif iroot.rank < jroot.rank:
            iroot, jroot = jroot, iroot
        jroot.parent = iroot
        iroot.size = iroot.size + jroot.size

    def size(self, i):
        return self._find(i).size

    class Node(object):
        def __init__(self):
            self.parent = self
            self.rank = 0
            self.size = 1

        def find(self):
            if self.parent != self:
                self.parent = self.parent.find()
            return self.parent


class Problem():

    def __init__(self):
        self.prime_minister = 524287
        self.res = 0
        self.random_generator = LaggedFibonnaciGenerator()
        self.disjoint_set = UnionFind()

    def get(self):
        while self.disjoint_set.size(524287) < 990000:
            caller = self.random_generator.next()
            called = self.random_generator.next()
            if caller != called:
                self.disjoint_set.union(caller, called)
                self.res += 1

    def solve(self):
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())