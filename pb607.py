import time
import sys
import math
import scipy.optimize


class Problem():

    def __init__(self):
        self.d = 50-25*math.sqrt(2)
        self.w = 10*math.sqrt(2)
        self.speeds = [10, 9, 8, 7, 6, 5, 10]
        self.res = 0

    def function_to_minimize(self, params):
        distances = [math.sqrt(params[0] ** 2 + (params[0] - self.d) ** 2)]
        for i in range(5):
            distances.append(math.sqrt((params[i+1]-params[i])**2+(params[i+1]-params[i]-self.w)**2))
        distances.append(math.sqrt((100-params[5])**2+(-params[5]+self.d+5*self.w)**2))
        lists_dist_speed = distances, self.speeds
        return sum([x / y for x, y in zip(*lists_dist_speed)])

    def get_res(self):
        initial_guess = [self.d+self.w*i for i in range(6)]
        result = scipy.optimize.minimize(self.function_to_minimize, initial_guess, tol=10**-10)
        if result.success:
            fitted_params = result.x
            self.res = round(self.function_to_minimize(fitted_params), 10)

    def solve(self):
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')


if __name__ == '__main__':
    sys.exit(main())
