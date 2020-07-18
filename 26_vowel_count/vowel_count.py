def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """
    freq = {}
    vowels = ['a', 'e', 'i', 'o', 'u']
    for vowel in vowels:
        count = phrase.lower().count(vowel)
        if count > 0:
            freq[vowel] = count
    return freq