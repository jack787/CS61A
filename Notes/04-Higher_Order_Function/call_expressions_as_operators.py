# Locally defined functions
def make_adder(n):
    """return a function that takes one argument k"""
    """ and return k+n"""

    def adder(k):
        return k + n

    return adder


square = lambda x: x * x


def compose1(f, g):
    def h(x):
        return f(g(x))

    return h


print(compose1(square, make_adder(2))(3))  # 25
