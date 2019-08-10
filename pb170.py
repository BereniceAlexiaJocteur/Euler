import time
import sys
import itertools


class Problem():

    def __init__(self):
        self.curr_max = 0

    def is_pandigital(self, n):
        n = str(n)
        return len(n) == 10 and not '1234567890'.strip(n)

    def get_max(self):
        for i in itertools.permutations(range(10)):
            for j in range(1, 9):
                first_term = int(''.join(map(str, i[:j])))
                for k in range(j+1, 10):
                    second_term = int(''.join(map(str, i[j:k])))
                    third_term = int(''.join(map(str, i[k:])))
                    if len(str(first_term)+str(second_term)+str(third_term)) != 10:
                        continue
                    first_prod = first_term*second_term
                    second_prod = first_term*third_term
                    result = int(str(first_prod)+str(second_prod))
                    if result > self.curr_max and self.is_pandigital(result):
                            self.curr_max = result

    def solve(self):
        self.get_max()
        print(self.curr_max)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())