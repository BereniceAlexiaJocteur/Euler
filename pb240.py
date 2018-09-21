import time
import sys
import itertools


class Problem():

    def __init__(self):
        self.number_dices = 20
        self.number_faces = 12
        self.sum_faces = 70
        self.top_numbers = 10
        self.factorial_list = [1]
        self.res = 0

    def init_factorial_list(self):
        fact = 1
        for i in range(1, self.number_dices + 1):
            fact *= i
            self.factorial_list.append(fact)

    def get_number_permutations(self, l):
        list_apparitions = [0] * self.number_faces
        for i in l:
            list_apparitions[i-1] += 1
        denominator = 1
        for i in list_apparitions:
            denominator *= self.factorial_list[i]
        return self.factorial_list[self.number_dices]//denominator

    def get_res(self):
        for i in itertools.combinations_with_replacement(range(1, self.number_faces+1), self.number_dices):
            if sum(i[-self.top_numbers:]) == self.sum_faces:
                self.res += self.get_number_permutations(i)

    def solve(self):
        self.init_factorial_list()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())