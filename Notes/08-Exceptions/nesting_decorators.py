from decorators import do_twice, timer


@do_twice
@timer
def greet(name):
    print(f"Hello {name}")


## shorthand that timer(do_twice(greet))
