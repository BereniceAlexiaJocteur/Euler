import time
import sys


class Problem():

    def __init__(self, n):
        self.n = n
        self.list_losing = [39, 43, 55, 59, 63]
        self.compteur = 13

    def get(self):
        u = self.list_losing[0] + 34
        while u <= self.n:
            self.compteur += 1
            self.list_losing.remove(self.list_losing[0])
            self.list_losing.append(u)
            u = self.list_losing[0] + 34
        return self.n - self.compteur

    def solve(self):
        print(self.get())


def main():
    start = time.perf_counter()
    u = Problem(10**6)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())