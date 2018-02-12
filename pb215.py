import time
import sys
import copy


class Problem():

    def __init__(self):
        self.number_lines = 10
        self.number_columns = 32
        self.possible_partitions = []
        self.possible_lines = []
        self.possible_neighbours = None
        self.res = 0

    def partition_min_max(self, n, k, l, m):
        """n is the integer to partition, k is the length of partitions,
        l is the min partition element size, m is the max partition element size """
        if k < 1:
            raise StopIteration
        if k == 1:
            if m >= n >= l:
                yield (n,)
            raise StopIteration
        for i in range(l, m+1):
            for result in self.partition_min_max(n-i, k-1, i, m):
                yield result+(i,)

    def init_possible_partitions(self):
        for i in range(self.number_columns//3, self.number_columns//2+1):
            l = list(self.partition_min_max(self.number_columns, i, 2, 3))
            if len(l) != 0:
                l1 = list(l[0])
                self.possible_partitions.append(l1)

    @staticmethod
    def number_of_2_and_3(li):
        le = len(li)
        i = 0
        while li[i] == 3:
            i += 1
        return le-i, i

    def f(self, l, n2, n3):
        if n2 == 0 and n3 == 0:
            return l
        elif n2 == 0:
            return self.f(l+[3], n2, n3-1)
        elif n3 == 0:
            return self.f(l+[2], n2-1, n3)
        else:
            return self.f(l+[3], n2, n3-1) + self.f(l+[2], n2-1, n3)

    def init_possible_lines(self):
        for i in self.possible_partitions:
            n2, n3 = self.number_of_2_and_3(i)
            tot = n2 + n3
            li = self.f([], n2, n3)
            for j in range(len(li)//tot):
                self.possible_lines.append(li[j*tot:(j+1)*tot])

    @staticmethod
    def can_be_neighbour(l1, l2):
        sum_l1 = []
        current_sum_l1 = 0
        sum_l2 = []
        current_sum_l2 = 0
        for i in range(len(l1)-1):
            current_sum_l1 += l1[i]
            sum_l1.append(current_sum_l1)
        for i in range(len(l2)-1):
            current_sum_l2 += l2[i]
            sum_l2.append(current_sum_l2)
        return set(sum_l1).isdisjoint(sum_l2)

    def init_possible_neighbours(self):
        cles = []
        for i in self.possible_lines:
            cles.append(''.join(str(e) for e in i))
        self.possible_neighbours = dict.fromkeys(cles)
        for i in self.possible_neighbours:
            li = [int(k) for k in list(i)]
            l = []
            for j in self.possible_lines:
                if self.can_be_neighbour(li, j):
                    l.append(j)
            self.possible_neighbours[i] = l

    def get_number_ways(self):
        cles = []
        for i in self.possible_lines:
            cles.append(''.join(str(e) for e in i))
        d1 = dict.fromkeys(cles, 1)
        for i in range(self.number_lines - 1):
            d2 = dict.fromkeys(cles, 0)
            for j in d1:
                for k in self.possible_neighbours[''.join(str(e) for e in j)]:
                    d2[''.join(str(e) for e in k)] += d1[''.join(str(e) for e in j)]
            d1 = copy.deepcopy(d2)
        for i in d1:
            self.res += d1[i]

    def solve(self):
        self.init_possible_partitions()
        self.init_possible_lines()
        self.init_possible_neighbours()
        self.get_number_ways()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())