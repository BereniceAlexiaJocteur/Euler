# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import time
import sys
import calendar

class Problem():

    def __init__(self, s):
        self.days = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
        self.n = self.days[s]

    def count_day(self):
        count = 0
        for year in range(1901, 2001):
            for month in range(1, 13):
                if calendar.weekday(year, month, 1) == self.n:
                    count += 1
        return count

    def solve(self):
        print(self.count_day())


def main():
    start = time.perf_counter()
    u = Problem('Sunday')
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())