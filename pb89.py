# -------------------------------------------------------------------------------
# Name:        pb89
# Purpose:     project euler
# Created:     18/02/2015
# -------------------------------------------------------------------------------

import time
import sys


def replace_all(text, dic):
    for i, j in dic.items():
        text = text.replace(i, j)
    return text


def main():
    start = time.perf_counter()
    a = open("p089_roman.txt").read()
    reps1 = {'DCCCC': 'CM', 'LXXXX': 'XC', 'VIIII': 'IX'}
    reps2 = {'CCCC': 'CD', 'XXXX': 'XL', 'IIII': 'IV'}
    new = replace_all(replace_all(a, reps1), reps2)
    print(len(a) - len(new))
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())