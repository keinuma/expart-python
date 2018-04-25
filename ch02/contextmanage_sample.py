from contextlib import contextmanager


class ContextIllustration:
    def __enter__(self):
        print('コンテキストに入ります')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('コンテキストから出ます')

        if exc_type is None:
            print('エラーはありません')
        else:
            print('エラーが (%s) 発生しました' % exc_val)


@contextmanager
def context_illustration():
    print('コンテキストに入ります')

    try:
        yield
    except Exception as e:
        print('コンテキストから出ます')
        print('エラー (%s) が発生しました' % e)
        # exception needs to be reraised
        raise
    else:
        print('コンテキストから出ます')
        print('エラーはありません')
