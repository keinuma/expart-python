import time
from functools import wraps
from random import randint
import matplotlib.pyplot as plt


def make_list(num):
    a = [randint(0, 1000) for _ in range(num)]
    return a


def func_times(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        elapsed_time = time.time() - start
        return result, elapsed_time
    return wrapper


@func_times
def sort_list(line):
    return line.sort()


@func_times
def get_max(line):
    return max(line)


@func_times
def append(line):
    return line.append(10)


@func_times
def len_list(line):
    return len(line)


@func_times
def in_list(line):
    return 10 in line


@func_times
def get_index(line):
    max_size = len(line)
    index = randint(0, max_size)
    return line[index - 1]


@func_times
def pop(line):
    line.pop()
    return None


def bench_mark(func):
    times = []
    x = range(1, 1000, 10)
    number = 100
    for i in x:
        tps = []
        for _ in range(number):
            line = make_list(i)
            _, temp = func(line )
            tps.append(temp)
        times.append(sum(tps) / number)
    plt.plot(x, times, label=func.__name__)
    plt.legend()
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('number')
    plt.ylabel('time')


if __name__ == '__main__':
    bench_mark(sort_list)
    bench_mark(append)
    bench_mark(pop)
    bench_mark(get_max)
    bench_mark(in_list)
    plt.show()
