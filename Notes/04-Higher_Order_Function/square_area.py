from math import pi, sqrt


def area_square(r):
    assert r > 0, "A length should be positive"
    return r * r


def area_circle(r):
    assert r > 0, "A length should be positive"
    return pi * r * r
