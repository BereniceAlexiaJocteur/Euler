import time
import sys
import math


class Problem():

    def __init__(self):
        self.numbers = [5678027, 7208785]
        self.primes_list = None
        self.triangular_numbers_list = None
        self.triangular_numbers_list_shift_plus = None
        self.triangular_numbers_list_shift_minus = None
        self.res = 0
        self.primes_set = None

    @staticmethod
    def triangular_number(n):
        return ((n+1)*n)//2

    def init_triangular_numbers(self, n):
        self.triangular_numbers_list = []
        for i in range(n-3, n+3):
            self.triangular_numbers_list.append(self.triangular_number(i))
        self.triangular_numbers_list_shift_plus = [i + 1 for i in self.triangular_numbers_list]
        self.triangular_numbers_list_shift_minus = [i - 1 for i in self.triangular_numbers_list]

    def potential_primes(self):
        ''' Make a generator for 2, 3, 5, & thence all numbers coprime to 30 '''
        s = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29)
        for i in s:
            yield i
        s = (1,) + s[3:]
        j = 30
        while True:
            for i in s:
                yield j + i
            j += 30

    def range_sieve(self, lo, hi):
        ''' Create a list of all primes in the range(lo, hi) '''
        # Mark all numbers as prime
        primes = [True] * (hi - lo)
        # Eliminate 0 and 1, if necessary
        for i in range(lo, min(2, hi)):
            primes[i - lo] = False
        ihi = int(hi ** 0.5)
        for i in self.potential_primes():
            if i > ihi:
                break
            # Find first multiple of i: i >= i*i and i >= lo
            ilo = max(i, 1 + (lo - 1) // i) * i
            # Determine how many multiples of i >= ilo are in range
            n = 1 + (hi - ilo - 1) // i
            # Mark them as composite
            primes[ilo - lo:: i] = n * [False]
        return [i for i, v in enumerate(primes, lo) if v]

    def init_primes(self):
        self.primes_list = self.range_sieve(self.triangular_numbers_list[0]+1, self.triangular_numbers_list[5])
        self.primes_set = set(self.primes_list)

    def primes_in_neighbourhood(self, x):
        count = 0
        value = None
        if x in self.triangular_numbers_list:
            ind = self.triangular_numbers_list.index(x)
            if self.triangular_numbers_list[ind-1] in self.primes_set:
                count += 1
                value = self.triangular_numbers_list[ind-1]
            for i in range(3):
                if self.triangular_numbers_list[ind+1]-i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind+1]-i
        elif x in self.triangular_numbers_list_shift_minus:
            ind = self.triangular_numbers_list_shift_minus.index(x)
            for i in range(2):
                if self.triangular_numbers_list[ind-1]-i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind-1]-i
            for i in range(1,4):
                if self.triangular_numbers_list[ind+1]-i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind+1]-i
        elif x in self.triangular_numbers_list_shift_plus:
            ind = self.triangular_numbers_list_shift_plus.index(x)
            for i in range(2):
                if self.triangular_numbers_list_shift_plus[ind-1]+i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind-1]+i
            for i in range(2):
                if self.triangular_numbers_list_shift_plus[ind+1]+i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind+1]+i
        else:
            min_val = min(filter(lambda i: i > x, self.triangular_numbers_list)) #plus petite valeure > x
            diff = min_val - x
            ind = self.triangular_numbers_list.index(min_val)
            for i in range(3):
                if self.triangular_numbers_list[ind-1] - diff + i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind-1] - diff + i
            for i in range(3):
                if self.triangular_numbers_list[ind+1] - diff - i in self.primes_set:
                    count += 1
                    value = self.triangular_numbers_list[ind+1] - diff - i
        if count >= 2:
            return 2, None
        elif count == 0:
            return 0, None
        else:
            return 1, value

    def s(self):
        curr_s = 0
        min_val = min(filter(lambda i: i > self.triangular_numbers_list[2], self.primes_list))
        min_ind = self.primes_list.index(min_val)
        max_val = max(filter(lambda i: i < self.triangular_numbers_list[3]+1, self.primes_list))
        max_ind = self.primes_list.index(max_val)
        for j in range(min_ind, max_ind+1):
            i = self.primes_list[j]
            number_primes_around = self.primes_in_neighbourhood(i)
            if number_primes_around[0] == 2:
                curr_s += i
            elif number_primes_around[0] == 1:
                if self.primes_in_neighbourhood(number_primes_around[1])[0] == 2:
                    curr_s += i
        return curr_s

    def solve(self):
        for n in self.numbers:
            self.init_triangular_numbers(n)
            self.init_primes()
            self.res += self.s()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())