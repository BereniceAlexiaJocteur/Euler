import time
import sys


class Problem():

    def __init__(self):  # a number is ambiguous if he is the MEAN of 2 consecutive terms in farey sequence
        self.res = 0
        self.r = 100
        self.bound = 10**8
        self.pairs = [[(0, 1), (1, 1), 2]]

    def get_res(self):
        while len(self.pairs):
            pair = self.pairs.pop()
            mid_denom = pair[2]
            mid_num = pair[0][0] * pair[1][1] + pair[0][1] * pair[1][0]
            if self.r * mid_num < mid_denom:
                self.res += 1
            med_num = pair[0][0] + pair[1][0]
            med_denom = pair[0][1] + pair[1][1]
            mediant = (med_num, med_denom)
            left_denom = 2 * pair[0][1] * med_denom
            right_denom = 2 * pair[1][1] * med_denom
            if left_denom <= self.bound:
                self.pairs.append([pair[0], mediant, left_denom])
            if right_denom <= self.bound and self.r*med_num < med_denom:
                self.pairs.append([mediant, pair[1], right_denom])

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
