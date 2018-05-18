# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import math
import time
import sys


class Problem():

    def __init__(self):
        self.ran = 10**10

    @staticmethod
    def squrt(n):
        return int(math.sqrt(n))

    def two_squares_sum_less_than(self, n):
        sum2sqs = [None]*(n+1)
        baseRt = self.squrt(n)
        for i in range(baseRt, -1, -1):
            for j in range(0, i+1):
                somme = i**2 + j**2
                if somme > n:
                    break
                else:
                    sumPair = [i, j]
                    sumLst = []
                    if sum2sqs[somme] is None:
                        sumLst = []
                        sum2sqs[somme] = sumLst
                    else:
                        sumLst = sum2sqs[somme]
                    sumLst.append(sumPair)
        result = []
        for nn in range(0, n+1):
            if sum2sqs[nn] is not None:
                result.append(sum2sqs[nn])
        return result

    def find_all_four_squares(self, n):
        sqr2s = self.two_squares_sum_less_than(n)
        hiList = []
        loList = []
        hp = []
        lp = []
        results = []
        prevHi = -1
        prevLo = -1
        hi = len(sqr2s) - 1
        lo = 0
        while hi >= lo:
            if hi != prevHi:
                hiList = sqr2s[hi]
                hp = hiList[0]
                hiSum = hp[0] * hp[0] + hp[1] * hp[1]
                prevHi = hi
            if lo != prevLo:
                loList = sqr2s[lo]
                lp = loList[0]
                loSum = lp[0] * lp[0] + lp[1] * lp[1]
                prevLo = lo
            if hiSum + loSum == n:
                for hiPair in hiList:
                    for loPair in loList:
                        quad = [None]*4
                        quad[0] = hiPair[0]
                        quad[1] = hiPair[1]
                        quad[2] = loPair[0]
                        quad[3] = loPair[1]
                        if quad[1] >= quad[2]:
                            results.append(quad)
                hi -= 1
                lo += 1
            elif hiSum + loSum < n:
                lo += 1
            else:
                hi -= 1
        return results

def main():
    start = time.time()
    u = Problem()
    print(u.find_all_four_squares(10**10))
    print('temps d execution', time.time() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())