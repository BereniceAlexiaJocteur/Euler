# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys


class Problem():

    def __init__(self):
        self.ran = 10**12
        self.num_5 = 0

    def get_num_5(self):
        s = 0
        p = 5
        t = self.ran // p
        while t > 0:
            s += t
            p *= 5
            t = t//p
        self.num_5 = s

    def get_res(self):
        num_2 = 0
        res = 1
        for i in range(1,self.ran+1):
            if i%(10**7)==0:
                print(i)
            j=i
            while j %5 == 0:
                j = j // 5
            while num_2 != self.num_5 and j%2 == 0:
                j = j// 2
                num_2 +=1
            res = (res*(j%10**5))%10**5
        print(res)

    def solve(self):
        self.get_num_5()
        self.get_res()


def main():
    start = time.time()
    u = Problem()
    u.solve()
    print('temps d execution', time.time() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())