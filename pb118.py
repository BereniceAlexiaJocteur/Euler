import itertools
import time
import sys
import primes


class Problem():

    def __init__(self):
        self.correct_primes = None
        self.res = 0

    def init_primes(self):  # initie le tableau des nombres premiers <987654321
        primes_numbers = primes.primes(987654321)
        self.correct_primes = set([x for x in primes_numbers if (
                    len(set(str(x))) == len(str(x)) and ('0' not in set(str(x))))])
        del primes_numbers

    def is_prime(self, n):  # renvoie si un entier est premier ou non en utilisant le tableau primes ou miller rabin suivant la taille du nombre
        return n in self.correct_primes

    def fonction_recursive(self, chiffres_restants, current_number, last_prime):
        if chiffres_restants == ():
            if current_number is None:
                return 1
            else:
                return 0
        else:
            if current_number is None:
                new_number = chiffres_restants[0]
            else:
                new_number = current_number*10+chiffres_restants[0]
            if self.is_prime(new_number) and (last_prime is None or new_number > last_prime):
                return self.fonction_recursive(tuple(list(chiffres_restants)[1:]), None, new_number) + self.fonction_recursive(tuple(list(chiffres_restants)[1:]), new_number, last_prime)
            else:
                return self.fonction_recursive(tuple(list(chiffres_restants)[1:]), new_number, last_prime)

    def solve(self):
        self.init_primes()
        for i in itertools.permutations(range(1, 10)):
            self.res += self.fonction_recursive(i, None, None)
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
