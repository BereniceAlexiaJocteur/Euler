import time
import sys
import primes


class Problem():

    def __init__(self):
        self.primes_list = None
        self.squbes_list = []
        self.res = 0

    def init_primes(self):
        self.primes_list = primes.sieve(2*10**5)

    def init_squbes_list(self):
        for p in self.primes_list:
            for q in self.primes_list:
                if p != q:
                    sqube = p**2*q**3
                    if "200" in str(sqube):
                        self.squbes_list.append(sqube)
        self.squbes_list.sort()

    def is_prime_proof(self, n):
        string_n = str(n)
        string_test = str(n)
        for i in range(1, 10):
            if i == string_n[0]:
                continue
            string_test = string_test[:0] + str(i) + string_test[1:]
            if primes.is_prime_opti(int(string_test)):
                return False
        for i in range(1, len(string_n)):
            string_test = str(n)
            for j in range(0, 10):
                if j == string_n[i]:
                    continue
                string_test = string_test[:i] + str(j) + string_test[i+1:]
                if primes.is_prime_opti(int(string_test)):
                    return False
        return True

    def get_res(self):
        count = 0
        for i in self.squbes_list:
            if self.is_prime_proof(i):
                count += 1
                if count == 200:
                    self.res = i
                    break

    def solve(self):
        self.init_primes()
        self.init_squbes_list()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())