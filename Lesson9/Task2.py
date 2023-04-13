class TypedMeta(type):
    a = None

    def __call__(cls, *args, **kwargs):
        if cls.a is None:
            cls.a = super().__call__()
        return cls.a


class MyClass(metaclass=TypedMeta):
    pass


if __name__ == '__main__':
    obj_1 = MyClass()
    obj_2 = MyClass()
    print(obj_1 is obj_2)
