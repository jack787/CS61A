def digit_pos_match(n, k):
    """
    >>> digit_pos_match(980, 0) # .Case 1
    True
    >>> digit_pos_match(980, 2) # .Case 2
    False
    >>> digit_pos_match(98276, 2) # .Case 3
    True
    >>> digit_pos_match(98276, 3) # .Case 4
    False
    """
    "*** YOUR CODE HERE ***"
    if n == 0 and k == 0:
        return True
    cnt = 0
    while n:
        if k == cnt and n % 10 == k:
            return True
        cnt += 1
        n //= 10
    return False


# print(digit_pos_match(980, 0))  # .Case 1

# print(digit_pos_match(980, 2))  # .Case 2

# print(digit_pos_match(98276, 2))  # .Case 3

# print(digit_pos_match(98276, 3))  # .Case 4
