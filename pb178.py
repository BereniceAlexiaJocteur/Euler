import time
import sys
import copy


class Problem():

    def __init__(self):
        self.number_digits = 40
        self.list_of_states = [(i, j, k) for i in range(10) for j in range(10) for k in range(i, j+1)]  # (min_reached, max_reached, current_digit)
        self.initial_states = [(i, i, i) for i in range(1, 10)]
        self.valid_final_states = [(0, 9, i) for i in range(10)]
        self.accesible_states = dict.fromkeys(self.list_of_states)
        self.res = 0

    def init_accesible_states(self):
        for k in self.list_of_states:  # on met les états qui sont accessibles à partir de k
            if k[2] == 9:
                if k[0] == 9:
                    self.accesible_states[k] = [(k[0] - 1, k[1], k[2] - 1)]
                else:
                    self.accesible_states[k] = [(k[0], k[1], k[2] - 1)]
            elif k[2] == 0:
                if k[1] == 0:
                    self.accesible_states[k] = [(k[0], k[1] + 1, k[2] + 1)]
                else:
                    self.accesible_states[k] = [(k[0], k[1], k[2] + 1)]
            else:
                if k[0] <= k[2]-1 and k[1] >= k[2]+1:
                    self.accesible_states[k] = [(k[0], k[1], k[2] - 1), (k[0], k[1], k[2] + 1)]
                elif k[0] == k[2] and k[1] >= k[2]+1:
                    self.accesible_states[k] = [(k[0] - 1, k[1], k[2] - 1), (k[0], k[1], k[2] + 1)]
                elif k[0] <= k[2]-1 and k[1] == k[2]:
                    self.accesible_states[k] = [(k[0], k[1], k[2] - 1), (k[0], k[1] + 1, k[2] + 1)]
                else:
                    self.accesible_states[k] = [(k[0] - 1, k[1], k[2] - 1), (k[0], k[1] + 1, k[2] + 1)]
        self.accesible_states[(0, 0, 0)] = self.initial_states  # on ne considère pas les nombres qui commencent par 0

    def get_number_ways(self):
        d1 = dict.fromkeys(self.list_of_states, 0)
        d1[(0, 0, 0)] = 1
        for i in range(self.number_digits):
            d2 = dict.fromkeys(self.list_of_states, 0)
            for j in d1:
                for k in self.accesible_states[j]:
                    d2[k] += d1[j]
            d1 = copy.deepcopy(d2)
            for w in self.valid_final_states:  # on compte les nombres de i-1 lettres qui sont validés
                self.res += d1[w]

    def solve(self):
        self.init_accesible_states()
        self.get_number_ways()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())