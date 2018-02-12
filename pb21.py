# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import eulerfun


class Problem():

    def __init__(self, n):
        self.lim = n + 1
        self.list_amicable = [None] * self.lim

    def get_sum_amicables(self):
        somme = 0
        for i in range(2, self.lim):
            temp = eulerfun.d(i)
            if temp < self.lim:
                if temp == i:
                    self.list_amicable[i] = False
                elif self.list_amicable[temp] is True:
                    continue
                elif self.list_amicable[temp] is None:
                    temp1 = eulerfun.d(temp)
                    if temp1 == i:
                        somme += i + temp
                        self.list_amicable[i] = True
                        self.list_amicable[temp] = True
                    else:
                        self.list_amicable[i] = False
                        self.list_amicable[temp] = False
                else:
                    continue
            else:
                temp1 = eulerfun.d(temp)
                if temp1 == i:
                    somme += i
        return somme

    def solve(self):
        print(self.get_sum_amicables())


def main():
    start = time.perf_counter()
    u = Problem(10000)
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())