import time
import sys
import fractions


class Problem():

    def __init__(self):
        self.numerateur = 123456789
        self.denominateur = 987654321
        self.tableau_resultat = []
        self.current_number = 1
        self.count = 0
        self.resultat = ""

    def get_resultat(self):
        pgcd = fractions.gcd(self.denominateur, self.numerateur)
        self.numerateur = self.numerateur // pgcd
        self.denominateur = self.denominateur // pgcd
        while self.denominateur != 1 or self.numerateur != 1:
            if self.numerateur > self.denominateur:
                self.numerateur -= self.denominateur
                if self.current_number == 0:
                    self.count += 1
                else:
                    self.tableau_resultat.append(self.count)
                    self.current_number = 0
                    self.count = 1
            else:
                self.denominateur -= self.numerateur
                if self.current_number == 1:
                    self.count += 1
                else:
                    self.tableau_resultat.append(self.count)
                    self.current_number = 1
                    self.count = 1
        if self.current_number == 1:
            self.count += 1
        else:
            self.tableau_resultat.append(self.count)
            self.current_number = 1
            self.count = 1
        self.tableau_resultat.append(self.count)
        self.tableau_resultat = self.tableau_resultat[::-1]
        self.resultat = ','.join(str(e) for e in self.tableau_resultat)

    def solve(self):
        self.get_resultat()
        print(self.resultat)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
