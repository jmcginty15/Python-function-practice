def find_factors(num):
    """Find factors of num, in increasing order.

    >>> find_factors(10)
    [1, 2, 5, 10]

    >>> find_factors(11)
    [1, 11]

    >>> find_factors(111)
    [1, 3, 37, 111]

    >>> find_factors(321421)
    [1, 293, 1097, 321421]
    """
    import math
    factors = []
    for i in range(1, int(math.sqrt(num))):
        j = int(num / i)
        if i * j == num:
            factors.append(i)
            factors.append(j)
    duplicates_removed = list(set(factors))
    duplicates_removed.sort()
    return duplicates_removed
