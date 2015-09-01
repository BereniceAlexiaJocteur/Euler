# -------------------------------------------------------------------------------
# Name:     pb336
# Purpose:  project euler
# Created:  19/02/2015
# -------------------------------------------------------------------------------

import itertools
import time
import sys


def main():
    start = time.perf_counter()
    counter = 0
    string = 'ABCDEFGHIJK'

    for i in itertools.permutations(string):
        if i[0] == 'A' or i[0] == 'B':
            continue
        j = i
        i = list(i)
        first_wrong = 0
        while first_wrong < len(string) and string[first_wrong] == i[first_wrong]:
            first_wrong += 1
        if first_wrong == len(string):
            continue
        move_counter = 0
        while first_wrong < len(string):
            right_char = string[first_wrong]
            index = i.index(right_char)
            if index == len(i) - 1:
                rev = i[first_wrong:len(i)]
                rev.reverse()
                i = i[0:first_wrong] + rev
            else:
                rev = i[index:len(i)]
                rev.reverse()
                i = i[0:index] + rev
            move_counter += 1
            while first_wrong < len(string) and string[first_wrong] == i[first_wrong]:
                first_wrong += 1
        if move_counter == 2*len(string) - 3:
            counter += 1
        if counter == 2011:
            print(j, "requires", move_counter, "moves, it is number", counter)
            break

    print('temps d execution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())