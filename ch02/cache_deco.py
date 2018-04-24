import time
import hashlib
import pickle


cache = {}


def is_obsolete(entry, duration):
    return time.time() - entry['time'] > duration


def compute_key(function, args, kw):
    key = pickle.dumps((function.__name__, args, kw))
    return hashlib.sha1(key).hexdigest()


def memoize(duration=10):
    def _memoize(function):
        def __memoize(*args, **kw):
            key = compute_key(function, args, kw)

            # 計算済みか
            if (key in cache and
                not is_obsolete(cache[key], duration)):
                print('キャッシュ済みの値を取得')
                return cache[key]['value']

            # 計算
            result = function(*args, **kw)
            # 結果の保存
            cache[key] = {
                'value': result,
                'time': time.time()
            }
            return result
        return __memoize
    return _memoize
