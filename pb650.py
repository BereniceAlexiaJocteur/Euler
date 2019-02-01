import sympy.ntheory
import collections
import time
import sys
import copy


class Problem():

    def __init__(self):
        self.res = 1  # enlève cas pathologique n=1
        self.n = 20000
        self.mod = 10**9 + 7
        self.curr_factorisation = dict()  # factorisation B(i-1) -> factorisation B(i)
        self.curr_sum_factors = None  # S(i-1) -> S(i)
        self.curr_factoriel_factorisation = dict()  # factorisation (i-1)! -> factorisation i!
        self.dico_inverse_primes_minus_1 = dict()  # inverse modulaire des pj-1
        self.list_factorisation_initiale = []  # en 0 factorisation de 2 en 1 celle de 3 etc
        self.list_factorisation_initiale_opposee = []  # en 0 factorisation de 2^(-1) en 1 celle de 3^(-1) etc

    @staticmethod
    def mult_dico(dic, alpha):
        # multiplie toutes les valeurs du dico par alpha
        dic1 = copy.deepcopy(dic)
        for x in dic1:
            dic1[x] *= alpha
        return dic1

    @staticmethod
    def add_two_dicos(dic1, dic2):
        # crée un dico avec les clés des deux dicos et ajoute les valeurs si clé en commun
        new_dico = copy.deepcopy(dic1)
        d1 = collections.Counter(new_dico)
        d2 = collections.Counter(dic2)
        d1.update(d2)
        return dict(d1)

    def init_list_factorisations(self):
        for i in range(2, self.n+1):
            self.list_factorisation_initiale.append(sympy.ntheory.factorint(i))
        self.list_factorisation_initiale_opposee = copy.deepcopy(self.list_factorisation_initiale)
        for i in range(len(self.list_factorisation_initiale_opposee)):
            self.list_factorisation_initiale_opposee[i] = self.mult_dico(self.list_factorisation_initiale_opposee[i],
                                                                         -1)

    def get_res(self):
        for i in range(2, self.n+1):
            self.curr_factoriel_factorisation = self.add_two_dicos(self.curr_factoriel_factorisation,
                                                                   self.list_factorisation_initiale_opposee[i-2])
            # calcul B(i)
            self.curr_factorisation = self.add_two_dicos(self.curr_factorisation,
                                                         self.mult_dico(self.list_factorisation_initiale[i-2], i))
            self.curr_factorisation = self.add_two_dicos(self.curr_factorisation, self.curr_factoriel_factorisation)
            # calcul de D(i) maintenant
            self.curr_sum_factors = 1
            for j in self.curr_factorisation:
                if j not in self.dico_inverse_primes_minus_1:
                    self.dico_inverse_primes_minus_1[j] = pow(j-1, self.mod-2, self.mod)
                self.curr_sum_factors = (self.curr_sum_factors*(
                        (pow(j, self.curr_factorisation[j]+1, self.mod)-1)*self.dico_inverse_primes_minus_1[j])) \
                                         % self.mod
            self.res = (self.res + self.curr_sum_factors) % self.mod

    def solve(self):
        self.init_list_factorisations()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
