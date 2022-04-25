def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        t = func(*args, **kwargs)
        # func(*args, **kwargs)
        return t

    return wrapper_do_twice


def do_twice1(func):
    def wrapper_do_twice(name):
        func(name)
        func(name)

    return wrapper_do_twice


def do_twice2(func):
    def wrapper_do_twice():
        func()
        func()

    return wrapper_do_twice
