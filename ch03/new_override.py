class InstanceCountingClass:
    instance_created = 0

    def __new__(cls, *args, **kwargs):
        print('__new__()が呼ばれました:', cls, args, kwargs)
        instance = super().__new__(cls)
        instance.number = cls.instance_created
        cls.instance_created += 1
        return instance

    def __init__(self, attribute):
        print('__init__()が呼ばれました:', self, attribute)
        self.attribute = attribute


class NoneZero(int):
    def __new__(cls, value):
        return super().__new__(cls, value) if value != 0 else None

    def __init__(self, skipped_value):
        """__init__実装はこの場合スキップされる可能性がある"""
        print('__init__()が呼ばれたんだ')
        super().__init__()
