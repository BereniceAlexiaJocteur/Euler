import time
import sys


class Problem():

    def __init__(self):
        self.A = "1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"
        self.B = "8214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196"
        self.length = len(self.A)
        self.fibo = [1]
        self.res = ""

    def init_fibo(self):
        a, b = 0, 1
        while b < 10**17:
            a, b = b, a+b
            self.fibo.append(b)

    def get_index_word(self, number):
        index = 0
        while self.length*self.fibo[index] <= number:
            index += 1
        return index

    def get_digit(self, number, word):
        if word == 0:
            return self.A[number]
        if word == 1:
            return self.B[number]
        delta = self.fibo[word - 2]*self.length
        if number < delta:
            return self.get_digit(number, word-2)
        else:
            return self.get_digit(number-delta, word-1)

    def d(self, n):
        return self.get_digit(n-1, self.get_index_word(n-1))

    def get_res(self):
        for n in range(18):
            self.res += str(self.d((127+19*n)*7**n))
        self.res = self.res[::-1]

    def solve(self):
        self.init_fibo()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
