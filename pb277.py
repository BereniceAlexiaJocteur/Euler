import time
import sys


class Problem():

    def __init__(self):
        self.sequence = "UDDDUdddDDUDDddDdDddDDUDDdUUDd"
        self.bound = 10**15
        self.step = 1
        self.res = None

    def subsequence_is_good(self, number, subsequence): # vérifie si le nombre correpond à la bonne lettre
        for curr_letter in subsequence:
            number_mod = number % 3
            if number_mod == 0:
                if curr_letter != 'D':
                    return False
                number //= 3
            if number_mod == 1:
                if curr_letter != 'U':
                    return False
                number = (4*number + 2)//3
            if number_mod == 2:
                if curr_letter != 'd':
                    return False
                number = (2*number - 1)//3
        return True

    def get_res(self):
        self.res = self.bound
        for length in range(1, len(self.sequence)+1):
            curr_sequence = self.sequence[:length]
            while not self.subsequence_is_good(self.res, curr_sequence):
                self.res += self.step
            self.step *= 3

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.time()
    u = Problem()
    u.solve()
    print('temps d execution', time.time() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())