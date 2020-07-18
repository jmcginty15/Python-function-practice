def remove_every_other(lst):
    """Return a new list of other item.

        >>> lst = [1, 2, 3, 4, 5]

        >>> remove_every_other(lst)
        [1, 3, 5]

    This should return a list, not mutate the original:

        >>> lst
        [1, 2, 3, 4, 5]
    """
    copy = lst.copy()
    for i in range(len(copy) - 1, -1, -1):
        print(i, i % 2, copy)
        if i % 2 == 1:
            copy.pop(i)
    return copy
