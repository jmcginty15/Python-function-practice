def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    indices = []
    s_vowels = []
    s_list = list(s)

    for i in range(len(s)):
        if s[i].lower() in vowels:
            indices.append(i)
            s_vowels.append(s[i])

    s_vowels.reverse()
    for i in range(len(indices)):
        s_list[indices[i]] = s_vowels[i]

    return ''.join(s_list)
