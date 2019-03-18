
Python O(n) Time

https://leetcode.com/problems/valid-palindrome-ii/discuss/107742

* Lang:    python3
* Author:  sparklethinker
* Votes:   0

```
def validPalindrome(self, s):
    """
    :type s: str
    :rtype: bool
    """
    def isPalindrome(s, lo, hi):
        """
        Return len(s) if it's palindrome; 
        otherwise return index where inconsistency occurs
        """
        if not s:
            return 0
        mid = (hi - lo) / 2
        for i in range(mid):
            if s[i + lo] != s[hi - 1 - i]:
                return i+lo
        return len(s)

    i = isPalindrome(s, 0, len(s))
    if i == len(s):
        return True
    if s[i + 1] == s[len(s) - 1 - i]:
        j = isPalindrome(s, i+2, len(s) - 1 - i)
        if j == len(s):
            return True
    if s[i] == s[len(s) - 2 - i]:
        j = isPalindrome(s, i + 1, len(s) - 2 - i)
        if j == len(s):
            return True 
    return False
```
