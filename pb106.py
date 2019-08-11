import time
import sys
import itertools


class Problem(): #on compte les paires de meme tailles pas complètements ordonnées (si on classe les deux paires il n'y a pas une dont les éléments plus petits que ceux en correspondace)

    def __init__(self, n):
        self.n = n
        self.res = 0

    def is_needed(self, B, C):
        for i in range(len(B)):
            if B[i] > C[i]:
                return True
        return False

    def get_res(self):
        for set_size in range(2, self.n // 2 + 1):
            for all_elements in itertools.combinations(range(self.n), 2 * set_size):
                for first_elements in itertools.combinations(all_elements, set_size):
                    if first_elements[0] != all_elements[0]:
                        continue
                    first_set = list(first_elements)
                    second_set = list(set(all_elements) - set(first_set))
                    second_set.sort()
                    if self.is_needed(first_set, second_set):
                        self.res += 1

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem(12)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())