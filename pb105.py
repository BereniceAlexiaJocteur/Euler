# -------------------------------------------------------------------------------
# Name:        pb105
# Purpose:     project euler
# Created:     16/07/2015
# -------------------------------------------------------------------------------

import itertools
import time
import sys


def test(s):
    l = len(s)
    for i in range(1, l):
        a = itertools.combinations(s, i)
        for x in a:
            setx = set(x)
            sumx = sum(int(item) for item in x)
            for j in range(1, l-i+1):
                b = itertools.combinations(s - setx, j)
                for y in b:
                    sumy = sum(int(item) for item in y)
                    if sumx == sumy:
                        return False
                    if (len(x) > len(y) and sumx <= sumy) or (len(y) > len(x) and sumy <= sumx):
                        return False
    return True


def main():
    start = time.perf_counter()
    with open("p105_sets.txt") as f:
        content = f.readlines()
    content = [x.strip('\n') for x in content]
    content = [x.split(',') for x in content]
    content = [set(x) for x in content]
    result = 0

    for k in range(len(content)):
        if test(content[k]):
            som = sum(int(item) for item in content[k])
            result += som

    print(result)
    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())