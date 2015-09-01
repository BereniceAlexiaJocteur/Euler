# -------------------------------------------------------------------------------
# Name:        
# Purpose:     
# Created:     
# -------------------------------------------------------------------------------

import fractions


class Problem():

    def __init__(self, order):
        self.order = order
        self.set_of_rationals = set()
        self.set_of_sums = set()
        self.total_fraction = 0

    def init_list(self):
        for i in range(2, self.order+1):
            for j in range(1, i):
                self.set_of_rationals.add(fractions.Fraction(j, i))

    @staticmethod
    def test_fi_and_n(n, x, y, z):
        list_fi = [x**(n+1)+y**(n+1)-z**(n+1), (x*y+x*z+y*z)*(x**(n-1)+y**(n-1)-z**(n-1)), x*y*z*(x**(n-2)+y**(n-2)-z*(n-2))]
        return list_fi[0] + list_fi[1] + list_fi[3] == 0

    def test(self):
        print(self.set_of_rationals)

u = Problem(35)
u.init_list()
u.test()