def isValid(s: str) -> bool:
    """
    Check if string has valid parentheses.
    Valid pairs: (), [], {}
    """
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in s:
        if char in mapping:
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
        else:
            stack.append(char)
    return not stack


# Test cases
if __name__ == "__main__":
    print(isValid("()"))        # True
    print(isValid("()[]{}"))    # True
    print(isValid("(]"))        # False
    print(isValid("([)]"))      # False
    print(isValid("{[]}"))      # True