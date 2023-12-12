import functools


def auth(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('new feature by deco')
        return func(*args, **kwargs)
    return inner


