def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    i = 0
    phrase_list = list(phrase)
    for char in phrase_list:
        if char.lower() == to_swap.lower():
            phrase_list[i] = char.swapcase()
        i += 1
    return ''.join(phrase_list)