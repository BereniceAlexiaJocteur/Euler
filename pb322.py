# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# ------------------------------------------------------------------------------

import time
import sys


def decimal_to_base(n, b):
    t = []
    d = n
    while d > 0:
        d, r = divmod(d, b)
        t.append(r)
    return t


def lucas_is_divisible_by_q(n, m, q):
    n2 = decimal_to_base(n, q)
    m2 = decimal_to_base(m, q)
    for k in range(len(n2)):
        if k > len(m2) - 1:
            temp = 0
        else:
            temp = m2[k]
        if n2[k] < temp:
            return True
    return False


def solve(m, n):
    count = 0
    for i in range(n, m):
        if lucas_is_divisible_by_q(i, n, 2) and lucas_is_divisible_by_q(i, n, 5):
            count += 1
    return count


def main():
    start = time.perf_counter()
    print(solve(10**9, 10**7-10))
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())
