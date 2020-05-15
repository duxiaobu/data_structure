from inspect import signature
from functools import wraps


def typeassert(*type_args, **type_kwargs):
    def wrap(func):
        sig = signature(func)
        bind_types = sig.bind_partial(*type_args, **type_kwargs).arguments
        print(bind_types)

        @wraps(func)
        def inner(*args, **kwargs):
            bind_values = sig.bind(*args, **kwargs).arguments.items()
            print(bind_values)
            for name, value in bind_values:
                if name in bind_types:
                    if not isinstance(value, bind_types[name]):
                        raise TypeError('Parameter: {} must be {}'.format(name, bind_types[name]))
            return func(*args, **kwargs)

        return inner

    return wrap


@typeassert(int, str, list)
def say(x, y, z):
    print(x, y, z)



if __name__ == '__main__':
    say(1, 'abc', [1, 2])
