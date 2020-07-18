def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    while len(parens) >= 1:
        if parens[0] == ')' or parens[-1] == '(':
            return False
        index = parens.find('()')
        parens = parens[:index] + parens[(index + 2):]
    return True
