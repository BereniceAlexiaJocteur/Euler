l=[1, 2, 2]
s = ''.join(str(e) for e in l)
print(s)
print([int(i) for i in list(s)])


def get_number_ways(self):
    d1 = dict.fromkeys(self.cle, 1)
    for i in range(self.number_lines - 1):
        d2 = dict.fromkeys(self.cle, 0)
        for j in d1:
            for k in self.possible_neighbours[''.join(str(e) for e in j)]:
                d2[''.join(str(e) for e in k)] += d1[''.join(str(e) for e in j)]
        d1 = copy.deepcopy(d2)
    for i in d1:
        self.res += d1[i]

    def init_cle(self):
        for i in self.possible_lines:
            self.cle.append(''.join(str(e) for e in i))
