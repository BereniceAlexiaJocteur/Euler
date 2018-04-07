import time
import sys
import primes
import math


class Problem():

    def __init__(self):
        self.primes = None
        self.res = 0
        self.limit = 999966663333

    def init_primes(self):
        self.primes = primes.primes(int(math.sqrt(self.limit))+100)

    def number_of_semidivisibles_beteween_consecutive_primes(self, p1, p2):
        return self.number_of_divisibles_between_bounds(p1**2+1, p2**2-1, p1)+self.number_of_divisibles_between_bounds(p1**2+1, p2**2-1, p2)-2*self.number_of_divisibles_between_bounds(p1**2+1, p2**2-1, p1*p2)

    def number_of_semidivisibles_beteween_consecutive_primes_modified(self, p1, p2):
        return self.number_of_divisibles_between_bounds(p1 ** 2 + 1, self.limit, p1) + self.number_of_divisibles_between_bounds(p1 ** 2 + 1, self.limit, p2) - 2*self.number_of_divisibles_between_bounds(p1 ** 2 + 1, self.limit, p1 * p2)

    def number_of_divisibles_between_bounds(self, lower_bound, upper_bound, divisor):
        a = lower_bound
        if a % divisor:
            a += divisor - (a % divisor)
        n = upper_bound // divisor - (lower_bound - 1) // divisor
        return n * (2 * a + (n - 1) * divisor) // 2

    def get_res(self):
        for i in range(len(self.primes)):
            p1 = self.primes[i]
            p2 = self.primes[i+1]
            if p2**2 <= self.limit:
                self.res += self.number_of_semidivisibles_beteween_consecutive_primes(p1, p2)
            else:
                self.res += self.number_of_semidivisibles_beteween_consecutive_primes_modified(p1, p2)
                break

    def solve(self):
        self.init_primes()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
