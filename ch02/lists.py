import time
import matplotlib.pyplot as plt
from functools import wraps
from operator import attrgetter
from random import randint
from collections import deque

import multiprocessing


def func_times(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        elapsed_time = time.time() - start
        return result, elapsed_time

    return wrapper


class ListCalc:
    """
    リストの各メソッドの計算量を計測する
    """

    def __init__(self):
        # ランダムに与えられた要素数の数値リストを作成
        self.col = None
        self.type = 'list'
        self.range = range(1, 10000, 100)

    @func_times
    def sort(self):
        return self.col.sort()

    @func_times
    def get_max(self):
        return max(self.col)

    @func_times
    def append(self):
        return self.col.append(12)

    @func_times
    def len_list(self):
        return len(self.col)

    @func_times
    def in_list(self):
        return 10 in self.col

    def get_index(self):
        max_size = len(self.col)
        index = randint(0, max_size)

        @func_times
        def inner():
            return self.col[index - 1] + 100
        return inner()

    @func_times
    def pop(self):
        self.col.pop()
        return None

    @func_times
    def popleft(self):
        self.col.pop(0)
        return None

    def replace(self):
        max_size = len(self.col)
        index = randint(0, max_size)

        @func_times
        def inner():
            self.col[index - 1] = 110
            return None
        return inner()

    @func_times
    def left_append(self):
        a = [12]
        return a + self.col

    def bench_mark(self, func_name):
        print(self.__class__, ' starting!')
        times = []
        func = attrgetter(func_name)(self)
        number = 100
        for i in self.range:
            tps = []
            for _ in range(number):
                self.col = [randint(0, 1000) for _ in range(i)]
                _, temp = func()
                tps.append(temp)
            times.append(sum(tps) / number)
        label = ' '.join([self.type, func_name])
        plt.plot(self.range, times, label=label)
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('number')
        plt.ylabel('time')


class DequeCalc(ListCalc):
    def __init__(self):
        super().__init__()
        self.type = 'deque'

    @func_times
    def left_append(self):
        return self.col.appendleft(12)

    @func_times
    def popleft(self):
        self.col.popleft()
        return None

    def bench_mark(self, func_name):
        print(self.__class__, ' starting!')
        times = []
        func = attrgetter(func_name)(self)
        number = 10
        for i in self.range:
            tps = []
            for _ in range(number):
                self.col = deque([randint(0, 1000) for _ in range(i)])
                _, temp = func()
                tps.append(temp)
            times.append(sum(tps) / number)
        label = ' '.join([self.type, func_name])
        plt.plot(self.range, times, label=label)
        plt.legend()
        plt.xscale('log')
        plt.yscale('log')
        plt.xlabel('number')
        plt.ylabel('time')


if __name__ == '__main__':
    list_a = ListCalc()
    deque_a = DequeCalc()
    f_name = 'get_index'

    exe1 = multiprocessing.Process(list_a.bench_mark(f_name))
    exe2 = multiprocessing.Process(deque_a.bench_mark(f_name))
    exe1.start()
    exe2.start()
    plt.show()
