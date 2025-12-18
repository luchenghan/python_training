def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i],0)
        countT[t[i]] = 1 + countT.get(t[i],0)

    for c in countS:
        if countS[c] != countT.get(c,0):
            return False
    return True

def isAnagramBySorted(s: str, t: str) -> bool:
    ss = sorted(s)
    tt = sorted(t)
    return ss == tt

def isAnagramByCounter(s: str, t: str) -> bool:
    from collections import Counter
    return Counter(s) == Counter(t)

if __name__ == "__main__":
    print(isAnagram("rat", "cat")) # false
    print(isAnagram("anagram", "nagaram")) # true

    print(isAnagramBySorted("rat", "cat")) # false
    print(isAnagramBySorted("anagram", "nagaram"))

    print(isAnagramByCounter("anagram", "nagaram"))# true