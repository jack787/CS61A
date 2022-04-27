from operator import ne


def neighbor_digits(num, prev_digit=-1):
    """
    Returns the number of digits in num that have the same digit to its right
    or left.
    >>> neighbor_digits(111)
    3
    >>> neighbor_digits(123)
    0
    >>> neighbor_digits(112)
    2
    >>> neighbor_digits(1122)
    4
    """
    "*** YOUR CODE HERE ***"
    if num < 10:
        return 0
    x = num % 10
    res = 0
    if x != prev_digit:
        prev_digit = x
        while num and num % 10 == prev_digit:
            res += 1
            num //= 10
        if res == 1:
            return neighbor_digits(num)
        if num == 0:
            return res
        else:
            res += neighbor_digits(num)

        return res
    ##solution
    if num < 10:
        return num == prev_digit
    last = num % 10
    rest = num // 10
    return int(prev_digit == last or rest % 10 == last) + neighbor_digits(
        num // 10, last
    )
