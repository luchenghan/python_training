def isPalindrome2(s: str) -> bool:
    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()
    return newStr == newStr[::-1]

def isPalindrome2(s: str) -> bool:
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not alphaNum(s[l]):
            l += 1
        while r > l and not alphaNum(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True

def alphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


if __name__ == "__main__":
    # test cases
    print(isPalindrome2("race a car")) # false
    print(isPalindrome2("A man, a plan, a canal: Panama")) # true