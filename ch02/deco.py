from functools import wraps


class WithoutDecorator:
    def some_static_method(self):
        print('これは静的なメソッドです')
    some_static_method = staticmethod(some_static_method)

    def some_class_method(self):
        print('これはクラスメソッドです')
    some_class_method = classmethod(some_class_method)


class WithDecorator:
    @staticmethod
    def some_static_method():
        print('これは静的なメソッドです')

    @classmethod
    def some_class_method(cls):
        print('これはクラスメソッドです')


# パラメータ付きのデコレータ
# デコレートするときは()必須
def repeat(number=3):
    """
    デコレートされた関数をnumberで指定された回数繰り返す
    最後に呼び出された関数の結果を、返り値に返す
    :param number: 繰り返し回数
    :return:
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


def dummy_decorator(function):
    # 元のfunctionの情報を保持
    @wraps(function)
    def wrapped(*args, **kwargs):
        """内部のラップ用関数のドキュメント"""
        return function(*args, **kwargs)
    return wrapped


@dummy_decorator
def function_with_important_doc():
    """なくなって欲しくない、重要なdocstring"""


rpc_info = {}


def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        # 引数情報の登録
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)

        def _check_types(elements, types):
            """肩をチェックするサブクラス"""
            if len(elements) != len(types):
                raise TypeError('引数の個数を間違えています')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                arg, of_the_right_type = couple
                if isinstance(arg, of_the_right_type):
                    continue
                raise TypeError(
                    '引数 #%d は %s 型である必要がります' % (index, of_the_right_type)
                )

        # ラップする関数
        def __xmlrpc(*args):  # キーワードは受け取れない
            # 入力チェックをする
            checkable_args = args[1:]  # selfを削除
            _check_types(checkable_args, in_)
            # 関数の実行
            res = function(*args)
            # 出力値のチェック
            if not type(res) in (tuple, list):
                checkable_res = (res,)
            else:
                checkable_res = res
            _check_types(checkable_res, out)

            # 関数と型のチェックが成功
            return res
        return __xmlrpc
    return _xmlrpc


class RPCView:
    @xmlrpc((int, int))  # int -> int
    def meth1(self, int1, int2):
        print('%d と %d を受け取りました' % (int1, int2))

    @xmlrpc((str,), (int,))  # string -> int
    def meth2(self, phrase):
        print('%s を受け取りました' % phrase)
        return 12
