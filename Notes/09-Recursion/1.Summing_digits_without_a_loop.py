def sum_digits(n):
    """
    >>> sum_digits(6)
    6
    >>> sum_digits(2021)
    5
    """
    if n < 10:
        return n
    else:
        all_but_last = n // 10
        last = n % 10
        return sum_digits(all_but_last) + last


print(sum_digits(2021))#5
