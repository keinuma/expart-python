class MetaClass(type):
    def __new__(mcs, name, bases, namespace):
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        return super().__call__(*args, **kwargs)


class RevealingMeta(type):
    def __new__(mcs, name, bases, namespace, **kwargs):
        print(mcs, '__new__が呼ばれました')
        return super().__new__(mcs, name, bases, namespace)

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(mcs, '__prepare__が呼ばれました')
        return super().__prepare__(name, bases, **kwargs)

    def __init__(cls, name, bases, namespace, **kwargs):
        print(cls, '__init__が呼ばれました')
        super().__init__(name, bases, namespace)

    def __call__(cls, *args, **kwargs):
        print(cls, '__call__が呼ばれました')
        return super().__call__(*args, **kwargs)


class RevealingClass(metaclass=RevealingMeta):
    def __new__(cls):
        print(cls, '__new__が呼ばれました')
        return super().__new__(cls)

    def __init__(self):
        print(self, '__init__が呼ばれました')
        super().__init__()
