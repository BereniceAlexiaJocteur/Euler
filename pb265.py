import sys
import time


class Problem:

    def __init__(self):
        self.number_of_digits = 5

    @staticmethod
    def binary_list_to_decimal(nums):
        number_binary = ''.join(map(str, nums))
        return int(number_binary, 2)

    def recursive_function(self, l, l_tuples):
        if len(l) == 2**self.number_of_digits:
            if (l[-4], l[-3], l[-2], l[-1], l[0]) not in l_tuples and (l[-3], l[-2], l[-1], l[-0], l[1]) not in \
                    l_tuples and (l[-2], l[-1], l[0], l[1], l[2]) not in l_tuples and (l[-1], l[0], l[1], l[2], l[3]) \
                    not in l_tuples:
                return self.binary_list_to_decimal(l)
            else:
                return 0
        else:
            if (l[-4], l[-3], l[-2], l[-1], 0) not in l_tuples:
                if (l[-4], l[-3], l[-2], l[-1], 1) not in l_tuples:
                    return self.recursive_function(l + [1], l_tuples + [(l[-4], l[-3], l[-2], l[-1], 1)]) + \
                           self.recursive_function(l + [0], l_tuples + [(l[-4], l[-3], l[-2], l[-1], 0)])
                else:
                    return self.recursive_function(l + [0], l_tuples + [(l[-4], l[-3], l[-2], l[-1], 0)])
            else:
                if (l[-2], l[-1], 1) not in l_tuples:
                    return self.recursive_function(l + [1], l_tuples + [(l[-4], l[-3], l[-2], l[-1], 1)])
                else:
                    return 0

    def solve(self):
        print(self.recursive_function([0, 0, 0, 0, 0], [(0, 0, 0, 0, 0)]))


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
