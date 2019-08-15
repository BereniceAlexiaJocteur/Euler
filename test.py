from fractions import Fraction


class Fr(Fraction):
    def __repr__(self):
        return '(%s/%s)' % (self.numerator, self.denominator)


def farey(n, length=False):
    if not length:
        return [Fr(0, 1)] + sorted({Fr(m, k) for k in range(1, n + 1) for m in range(1, k + 1)})
    else:
        # return 1         +    len({Fr(m, k) for k in range(1, n+1) for m in range(1, k+1)})
        return (n * (n + 3)) // 2 - sum(farey(n // k, True) for k in range(2, n + 1))



print(farey(10**5))
