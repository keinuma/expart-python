from threading import RLock


lock = RLock()


def synchronized(function):
    def _synchronized(*args, **kw):
        lock.acquire()
        try:
            return function(*args, **kw)
        finally:
            lock.release()
    return _synchronized


@synchronized
def thread_safe():  #リソースがロックされていることを保証する
    pass


class MyClass:
    """my docstring"""
    pass


my = MyClass()


# インスタンスにメソッドを追加する
def addto(instance):
    def _addto(f):
        import types
        f = types.MethodType(f, instance)
        setattr(instance, f.__name__, f)
        return f
    return _addto


@addto(my)
def print_docstring(self):
    print(self.__doc__)


def print_args(f):
    def _print_args(*args, **kw):
        print(f.__name__, args, kw)
        return f(*args, **kw)
    return _print_args


@print_args
def my_function(a, b, c):
    print(a + b, c * 2)
