def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    freq1 = {}
    freq2 = {}
    str1 = str(num1)
    str2 = str(num2)
    
    for digit in str1:
        if not digit in freq1:
            freq1[digit] = str1.count(digit)
    for digit in str2:
        if not digit in freq2:
            freq2[digit] = str2.count(digit)
    
    for key in freq1:
        if not key in freq2:
            return False
        elif freq1[key] != freq2[key]:
            return False
    return True