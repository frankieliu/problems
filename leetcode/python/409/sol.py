
Python using replace (99%)

https://leetcode.com/problems/longest-palindrome/discuss/89628

* Lang:    python3
* Author:  jial1
* Votes:   0

Somehow I found the replace method surprisingly fast for several problems. In this problem, for each letter (ss) in s (starting from s[0]), I first remove all ss in s ( s.replace(ss,'') ), and compare the length of the string before and after, and increase the palindrome length by the difference (or difference-1 if it's a odd number).

Finally, if the palindrome length is even, and I happen to removed an odd number of letters, I add 1 to the end.

```
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        lp=0
        n0=len(s)
        while n0 > 0:
            ss=s[0]
            s=s.replace(ss,'')
            n1=len(s)
            lp += 2*int((n0-n1)/2)
            if lp%2==0 and (n0-n1)%2:
                lp+=1
            n0=n1
        return lp
```
