import time
import sys
import random


class Problem():

    def __init__(self):
        self.list_test = ["5616185650518293",
                          "3847439647293047",
                          "5855462940810587",
                          "9742855507068353",
                          "4296849643607543",
                          "3174248439465858",
                          "4513559094146117",
                          "7890971548908067",
                          "8157356344118483",
                          "2615250744386899",
                          "8690095851526254",
                          "6375711915077050",
                          "6913859173121360",
                          "6442889055042768",
                          "2321386104303845",
                          "2326509471271448",
                          "5251583379644322",
                          "1748270476758276",
                          "4895722652190306",
                          "3041631117224635",
                          "1841236454324589",
                          "2659862637316867"]
        self.list_result_test = [2,
                                 1,
                                 3,
                                 3,
                                 3,
                                 1,
                                 2,
                                 3,
                                 1,
                                 2,
                                 3,
                                 1,
                                 1,
                                 2,
                                 0,
                                 2,
                                 2,
                                 3,
                                 1,
                                 3,
                                 3,
                                 2]
        self.number_of_guesses = len(self.list_test)
        self.length = len(self.list_test[0])
        self.population_size = 1000
        self.civilizations = 100
        self.generations = 100
        self.mutation_rate = 0.5
        self.res = 0

    def distance(self, state):  # distance between state and the sample given
        c = 0
        for i in range(self.number_of_guesses):
            same_digits = sum(state[j] == self.list_test[i][j] for j in range(self.length))
            c += abs(same_digits - self.list_result_test[i])
        return c

    @staticmethod
    def weighted_choice(states, scores):
        total = sum(scores)
        r = random.uniform(0, total)
        running_sum = 0.0
        for c, w in zip(states, scores):
            if running_sum + w >= r:
                return c
            running_sum += w

    def random_state(self):
        return str(10 ** self.length + random.randint(0, 10 ** self.length - 1))[1:]

    def get_child(self, p1, p2):
        """
        Given a two parents and a mutation rate, returns a child with each character taken at random
        from a parent, with a chance of having a single character mutated into a random digit.
        """
        c = ''
        for x, y in zip(p1, p2):
            if random.randint(0, 1):
                c += x
            else:
                c += y
        if random.random() < self.mutation_rate:
            a = random.randint(0, len(c) - 1)
            b = str(random.randint(0, 9))
            c = c[:a] + b + c[a + 1:]
        return c

    def get_res(self):
        for civ in range(self.civilizations):
            initial_population = [self.random_state() for _ in range(self.population_size)]
            pop_and_cost = [(p, self.distance(p)) for p in initial_population]
            for g in range(self.generations):
                # Sort population by increasing cost
                pop_and_cost.sort(key=lambda x: x[1])
                # Check for full solution
                if pop_and_cost[0][1] == 0:
                    self.res = pop_and_cost[0][0]
                    print(pop_and_cost[0])
                    return
                # Cull population back down to population size
                del pop_and_cost[self.population_size:]
                # Assign fitness scores to current population (only needed with weighted parent selection)
                pop, fitness = [p for p, _ in pop_and_cost], [1.0 / c for _, c in pop_and_cost]
                for _ in range(self.population_size):
                    # Pick two parents
                    parent1 = self.weighted_choice(pop, fitness)
                    parent2 = self.weighted_choice(pop, fitness)
                    # Make a child and add it to population along with its cost
                    child = self.get_child(parent1, parent2)
                    pop_and_cost.append((child, self.distance(child)))
            print(pop_and_cost[0])
        self.res = "fail"

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
