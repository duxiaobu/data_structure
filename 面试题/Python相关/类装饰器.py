class Logger:
    def __init__(self, name):
        self.name = name

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance


def single(cls):
    _instance = {}

    def wrap(*args, **kwargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kwargs)
        return _instance[cls]

    return wrap


@single
class Child:
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    l1 = Logger("bob")
    print(l1.name, id(l1))
    l2 = Logger("jack")
    print(l2.name, id(l2))
    print(id(l1), id(l2))
