import time
import sys
import fractions


class Problem():

    def __init__(self):
        self.sn = 290797  # initialisation à s0
        self.tn_list = []
        self.list_a_b = []  # a coeff directeur et b abcisse origine
        self.set_intersections = set()  # UNE INTERSECTION PEUT APPARAITRE PLUSIEURS FOIS -> utiliser un set

    def init_tn(self):
        for i in range(5000):
            quadruplet = []
            for j in range(4):
                self.sn = (self.sn**2) % 50515093
                quadruplet.append(self.sn % 500)
            self.tn_list.append(quadruplet)

    def init_list_a_b(self):  # prend en argument un quadruplet (x1,y1,x2,y2) pour retourner le couple coeef
        # directeur + abcisse origine OU un singleton (a) si équation de la forme x = a
        for liste in self.tn_list:
            x1 = liste[0]
            y1 = liste[1]
            x2 = liste[2]
            y2 = liste[3]
            if x1 != x2:
                a = fractions.Fraction((y2-y1), (x2-x1))
                b = y1 - a*x1
                self.list_a_b.append((a, b))
            else:                                             # ce cas arrive bien !!
                self.list_a_b.append(tuple([x1]))

    def get_intersection(self, i, j):  # renvoie l'intersection du i eme SEGMENT avec le j eme SI ELLE EXISTE ET EST
        # A L INTERIEUR DES SEGMENTS
        li = self.list_a_b[i]
        lj = self.list_a_b[j]
        s = len(li)+len(lj)
        x1 = self.tn_list[i][0]
        y1 = self.tn_list[i][1]
        x2 = self.tn_list[i][2]
        y2 = self.tn_list[i][3]
        x1_prime = self.tn_list[j][0]
        y1_prime = self.tn_list[j][1]
        x2_prime = self.tn_list[j][2]
        y2_prime = self.tn_list[j][3]
        #  on détermine les coordonées de l'intersection : None si elle existe pas ou pas unique
        if s == 2:
            return None
        elif s == 3:
            if len(li) == 2:
                x = lj[0]
                y = li[0]*x + li[1]
                intersection = (x, y)
                #  vérifier si intersection A L INTERIEUR DES 2 SEGMENTS
                if li[0] == 0:  # si la droite pas verticale est horizontale
                    if min(x1, x2) < x < max(x1, x2) and min(y1_prime, y2_prime) < y < max(y1_prime, y2_prime):
                        return intersection
                    else:
                        return None
                else:  # si la droite pas verticale n'est pas horizontale non plus
                    if min(x1, x2) < x < max(x1, x2) and min(y1, y2) < y < max(y1, y2) and \
                            min(y1_prime, y2_prime) < y < max(y1_prime, y2_prime):
                        return intersection
                    else:
                        return None
            else:
                x = li[0]
                y = lj[0] * x + lj[1]
                intersection = (x, y)
                #  vérifier si intersection A L INTERIEUR DES 2 SEGMENTS
                if lj[0] == 0:  # si la droite pas verticale est horizontale
                    if min(x1_prime, x2_prime) < x < max(x1_prime, x2_prime) and min(y1, y2) < y < max(y1, y2):
                        return intersection
                    else:
                        return None
                else:  # si la droite pas verticale n'est pas horizontale non plus
                    if min(x1_prime, x2_prime) < x < max(x1_prime, x2_prime) and \
                            min(y1_prime, y2_prime) < y < max(y1_prime, y2_prime) and min(y1, y2) < y < max(y1, y2):
                        return intersection
                    else:
                        return None
        elif s == 4:
            a1 = li[0]
            b1 = li[1]
            a2 = lj[0]
            b2 = lj[1]
            if a1 == a2:
                return None
            else:
                x = (b2-b1) / (a1-a2)
                y = a1*x + b1
                intersection = (x, y)
                #  vérifier si intersection A L INTERIEUR DES 2 SEGMENTS
                if a1 == 0:  # si la première droite est horizontale
                    if min(x1, x2) < x < max(x1, x2) and min(x1_prime, x2_prime) < x < max(x1_prime, x2_prime) and \
                            min(y1_prime, y2_prime) < y < max(y1_prime, y2_prime):
                        return intersection
                    else:
                        return None
                elif a2 == 0:  # si la seconde droite est horizontale
                    if min(x1_prime, x2_prime) < x < max(x1_prime, x2_prime) and min(x1, x2) < x < max(x1, x2) and \
                            min(y1, y2) < y < max(y1, y2):
                        return intersection
                    else:
                        return None
                else:  # si aucune droite est horizontale
                    if min(x1_prime, x2_prime) < x < max(x1_prime, x2_prime) \
                            and min(y1_prime, y2_prime) < y < max(y1_prime, y2_prime) and min(x1, x2) < x < max(x1, x2)\
                            and min(y1, y2) < y < max(y1, y2):
                        return intersection
                    else:
                        return None

    def init_set_intersections(self):
        for i in range(5000):
            for j in range(i):
                self.set_intersections.add(self.get_intersection(i, j))

    def solve(self):
        self.init_tn()
        self.init_list_a_b()
        self.init_set_intersections()
        print(len(self.set_intersections)-1)  # -1 pour enlever None du set


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
