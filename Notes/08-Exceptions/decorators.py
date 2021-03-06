def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        t = func(*args, **kwargs)
        # func(*args, **kwargs)
        func(*args, **kwargs)
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


import functools
import time


def timer(func):
    """Print the runtime of the decorated function"""

    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finish {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer


def repeat(num_times):
    def decorator_repeat(func):
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    return decorator_repeat


def repeat2(_func=None, *, num_times=2):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value

        return wrapper_repeat

    if _func is None:
        return decorator_repeat
    else:
        return decorator_repeat(_func)
