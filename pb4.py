# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self, n):
        self.lim = n

    @staticmethod
    def is_palindrome(n):
        s = ''
        ns = str(n)
        for letter in ns:
            s = letter + s
        return s == ns

    def get_largest_palindrome(self):
        largest_palindrome = 0
        for i in range(10**self.lim-1, 10**(self.lim-1), -1):
            for j in range(10**self.lim-1, i, -1):
                if self.is_palindrome(str(i*j)) and i*j > largest_palindrome:
                    largest_palindrome = i*j
        return largest_palindrome

    def solve(self):
        print(self.get_largest_palindrome())


def main():
    start = time.perf_counter()
    u = Problem(3)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())