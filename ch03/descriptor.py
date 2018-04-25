class RevealAccess(object):
    """
    通常と同じようにデータの設定を行うが、
    アクセスされたログメッセージを残すデータディスクリプタ
    """

    def __init__(self, initval=None, name='var'):
        self.val = initval
        self.name = name

    def __get__(self, obj, objtype):
        print('取得:', self.name)
        return self.val

    def __set__(self, obj, val):
        print('更新:', self.name)
        self.val = val


class MyClass(object):
    x = RevealAccess(10, '変数 "x"')
    y = 5


class InitOnAccess:
    def __init__(self, klass, *args, **kwargs):
        self.klass = klass
        self.args = args
        self.kwargs = kwargs
        self._initialized = None

    def __get__(self, instance, owner):
        if self._initialized is None:
            print('初期化')
            self._initialized = self.klass(*self.args, **self.kwargs)
        else:
            print('キャッシュ済み!')
        return self._initialized
