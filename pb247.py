import time
import sys
import math


class Problem():

    def __init__(self):
        self.min_size = 1
        self.res = 0

    def get_next_states_1(self, prev_state):
        x0, y0 = prev_state['origin']
        i, j = prev_state['index']
        size = prev_state['size']
        x0top, y0top = x0, y0+size
        itop, jtop = i, j+1
        sizetop = 0.5*(math.sqrt((x0top-y0top)**2+4)-x0top-y0top)
        x0right, y0right = x0+size, y0
        iright, jright = i+1, j
        sizeright = 0.5 * (math.sqrt((x0right - y0right) ** 2 + 4) - x0right - y0right)
        return {'origin': (x0right, y0right), 'index': (iright, jright), 'size': sizeright}, {'origin': (x0top, y0top),
                                                                                              'index': (itop, jtop),
                                                                                              'size': sizetop}

    def get_min_size(self):
        stack = [{'origin': (1, 0), 'index': (0, 0), 'size': 0.5*(math.sqrt(1+4)-1)}]
        while stack:
            top = stack.pop()
            i, j = top['index']
            if i > 3 or j > 3:
                continue
            if i == 3 and j == 3:
                self.min_size = min(self.min_size, top['size'])
                continue
            right_state, up_state = self.get_next_states_1(top)
            stack.append(right_state)
            stack.append(up_state)

    def get_next_states_2(self, prev_state):
        x0, y0 = prev_state['origin']
        size = prev_state['size']
        x0top, y0top = x0, y0 + size
        sizetop = 0.5 * (math.sqrt((x0top - y0top) ** 2 + 4) - x0top - y0top)
        x0right, y0right = x0 + size, y0
        sizeright = 0.5 * (math.sqrt((x0right - y0right) ** 2 + 4) - x0right - y0right)
        return {'origin': (x0right, y0right), 'size': sizeright}, {'origin': (x0top, y0top), 'size': sizetop}

    def get_res(self):
        stack = [{'origin': (1, 0), 'size': 0.5 * (math.sqrt(1 + 4) - 1)}]
        while stack:
            top = stack.pop()
            if top['size'] < self.min_size:
                continue
            self.res += 1
            left_state, up_state = self.get_next_states_2(top)
            stack.append(left_state)
            stack.append(up_state)

    def solve(self):
        self.get_min_size()
        self.get_res()
        print(self.res)


def main():
    start = time.perf_counter()
    u = Problem()
    u.solve()
    print('temps d\'exécution', time.perf_counter() - start, 'sec')

if __name__ == '__main__':
    sys.exit(main())