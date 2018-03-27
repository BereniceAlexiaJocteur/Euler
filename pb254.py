import sys
import time


class Problem:

    def __init__(self):
        self.list_factorial = []
        self.dict_test = dict()
        self.somme = 0
        self.limit = 150
        self.profondeur_limite = 20

    def init_list_factorial(self):
        self.list_factorial.append(1)
        curr_fact = 1
        for i in range(1, 10):
            curr_fact *= i
            self.list_factorial.append(curr_fact)

    def init_dict(self):
        self.dict_test = dict.fromkeys(range(1, self.limit+1))
        for i in self.dict_test:
            self.dict_test[i] = -1

    def sum_digits(self, n):
        r = 0
        while n:
            r, n = r + n % 10, n // 10
        return r

    def number_zeros(self, n):
        s = 0
        while n:
            r = n % 10
            n = n//10
            if r == 0:
                s += 1
        return s

    def sum_digits_factorial(self, n):
        r = 0
        while n:
            r, n = r + self.list_factorial[n % 10], n // 10
        return r

    def list_to_int(self, l):
        r = 0
        for i in l:
            r = r*10+i
        return r

    def get_min_number(self, l, num_zeros):
        l1 = sorted(l)
        l0 = [0]*num_zeros
        list_res = [l1[0]]+l0+l1[1:]
        return self.list_to_int(list_res)

    def flatten(self, S):
        if S == []:
            return S
        if isinstance(S[0], list):
            return self.flatten(S[0]) + self.flatten(S[1:])
        return S[:1] + self.flatten(S[1:])

    def flatten2(self, l):
        for el in l:
            if isinstance(el, list):
                yield from self.flatten2(el)
            else:
                yield el

    def get_dict_recursif(self, profondeur_actuelle, i_actuel, l_actuel):
        if profondeur_actuelle == self.profondeur_limite:
            number_initial = self.list_to_int(l_actuel)
            nzero = self.number_zeros(number_initial)
            s1 = self.sum_digits_factorial(number_initial)
            for z in range(nzero + 1):
                s2 = s1 - z
                list_without_zero = sorted(l_actuel)[z:]
                s3 = self.sum_digits(s2)
                mnumber = self.get_min_number(list_without_zero, z)
                if s3 in range(1, self.limit + 1):
                    return s3, mnumber
        else:
            return list(set(self.flatten2(list(self.get_dict_recursif(profondeur_actuelle+1, j, l_actuel+[j])for j in range(i_actuel, 10)))))

    def fill_dict(self):
        for i in self.get_dict_recursif(0, 0, []):
            if i is not None:
                if self.dict_test[i[0]] == -1 or i[1] < self.dict_test[i[0]]:
                    self.dict_test[i[0]] = i[1]

    def get_somme(self):
        for i in self.dict_test:
            if self.dict_test[i] == -1:
                print("stop "+str(i))
                break
            self.somme += self.sum_digits(self.dict_test[i])

    def solve(self):
        self.init_list_factorial()
        self.init_dict()
        self.fill_dict()
        self.get_somme()
        print(self.somme)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d execution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
