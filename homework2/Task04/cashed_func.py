"""
Write a function that accepts another function as an argument. Then it
should return such a function, so the every call to initial one
should be cached.
def func(a, b):
    return (a ** b) ** 2
cache_func = cache(func)
some = 100, 200
val_1 = cache_func(*some)
val_2 = cache_func(*some)
assert val_1 is val_2
"""
from collections.abc import Callable


def cache(function: Callable) -> Callable:
    dict = {}

    def wrapper(*args):
        if dict.get(args):
            result = dict.get(args)
        else:
            result = function(*args)
            dict[args] = result
        return result

    return wrapper


def func(a, b):
    ans = (a ** b) ** 2
    print("real invocation")
    return ans


cached_func = cache(func)  # I don't know other way how to test it yet

print(cached_func(3, 2))
print(cached_func(3, 2))
