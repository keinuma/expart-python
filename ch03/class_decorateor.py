def short_repr(cls):
    cls.__repr__ = lambda self: super(cls, self).__repr__()[:8]
    return cls


def parametrized_short_repr(max_width=8):
    """文字列表現を短縮する、パラメータつきデコレータ"""
    def parametrized(cls):
        """実際のデコレータとして使用される内部ラッパー関数"""
        class ShortRepresented(cls):
            """デコレートされた動作を提供するサブクラス"""
            def __repr__(self):
                return super().__repr__()[:max_width]
        return ShortRepresented
    return parametrized


@short_repr
class ClassWithRelativeLongName:
    pass


@parametrized_short_repr(10)
class ClassWithLittleBitLongerLongName:
    pass
