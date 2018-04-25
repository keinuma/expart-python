class CommonBase:
    def method(self):
        print('CommonBase')


class Base1(CommonBase):
    pass


class Base2(CommonBase):
    def method(self):
        print('Base2')


class MyClass(Base1, Base2):
    pass


def L(klass):
    return [k.__name__ for k in klass.__mro__]
