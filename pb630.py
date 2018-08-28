import time
import sys
import fractions


class Problem():

    def __init__(self):
        self.sn = 290797
        self.tn_list = []
        self.mod1 = 50515093
        self.mod2 = 2000
        self.n = 2500
        self.slope_dictionnary = dict()
        self.res = 0

    def init_list_tn(self):
        for i in range(self.n):
            self.sn = (self.sn**2) % self.mod1
            t1 = (self.sn % self.mod2) - 1000
            self.sn = (self.sn ** 2) % self.mod1
            t2 = (self.sn % self.mod2) - 1000
            self.tn_list.append((t1, t2))

    def init_slope_dictionnary(self):
        for i in range(len(self.tn_list)-1):
            x1 = self.tn_list[i][0]
            y1 = self.tn_list[i][1]
            for j in range(i+1, len(self.tn_list)):
                x2 = self.tn_list[j][0]
                y2 = self.tn_list[j][1]
                if x2 != x1:
                    slope = fractions.Fraction(y1 - y2, x2 - x1)
                else:
                    slope = "vertical"
                try:
                    liste = list(self.slope_dictionnary[slope])
                    if (x1, y1) not in liste:
                        liste.append((x1, y1))
                        if (x2, y2) not in liste:
                            liste.append((x2, y2))
                            liste[0] += 1
                    if (x2, y2) not in liste:
                        liste.append((x2, y2))
                    self.slope_dictionnary[slope] = tuple(liste)
                except KeyError:
                    self.slope_dictionnary[slope] = (1, (x1, y1), (x2, y2))

    def get(self):
        m = sum(i[0] for i in self.slope_dictionnary.values())
        first_term = ((m-1)*m)
        second_term = sum(((s[0]-1)*s[0]) for s in self.slope_dictionnary.values())
        self.res = first_term - second_term

    def solve(self):
        self.init_list_tn()
        self.init_slope_dictionnary()
        self.get()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())