"""
2.1 pythonの組み込み型
"""

import time
import timeit
from functools import wraps

TIMES = 10000

SETUP = """
DELIMITER = ','
SUBSTRINGS = ['いくつかの', 'カンマ', '区切りの', '値']
sub = SUBSTRINGS * int({num})

def loop_join(substrings):
    s = ''
    for substring in substrings:
        s += substring
    return s


def method_join(delimiter, substrings):
    del_join = delimiter.join(substrings)
    return del_join
"""


def func_times(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        elapsed_time = time.time() - start
        print('{}は{}かかったぜよ'.format(f.__name__, elapsed_time))
        return result

    return wrapper


def byte_check():
    # バイナリデータ
    print(bytes([102, 111, 111]))
    # バイナリをリストに変換
    byte_list = list(b'foo bar')
    print('byte_list =', byte_list)
    print(type('何らかの文字列'))
    array = bytearray([102, 123, 210])
    print(type(array))

    # 文字列型からバイナリに変換
    ja_str = 'フランス'
    ja_byte = ja_str.encode()
    print(ja_byte, type(ja_byte))

    ja_byte2 = bytes(ja_str, 'utf-8')
    print(ja_byte == ja_byte2)

    # バイナリから文字列に変換
    print('バイナリから文字列に変換', ja_byte.decode())
    print(ja_byte.decode() == str(ja_byte2, 'utf-8'))


def clock(label, cmd, num):
    res = timeit.repeat(cmd, setup=SETUP.format_map({'num': num}), number=TIMES, repeat=3)
    print('文字列数: ', int(num * 4))
    print(label, *('{:.3f}'.format(x) for x in res))


def bench_mark(num):
    clock('forループ結合: ', 'loop_join(substrings=sub)', num)
    clock('joinメソッド : ', 'method_join(delimiter=DELIMITER, substrings=sub)', num)


if __name__ == '__main__':
    bench_mark(10)
