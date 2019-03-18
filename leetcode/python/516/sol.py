
Fast and concise Python solution that actually gets AC

https://leetcode.com/problems/longest-palindromic-subsequence/discuss/99153

* Lang:    python3
* Author:  o_sharp
* Votes:   20

I noticed that some of the most voted python solutions here got TLE, so here is an optimized solution.
```
class Solution(object):
    def longestPalindromeSubseq(self, s):
        d = {}
        def f(s):
            if s not in d:
                maxL = 0    
                for c in set(s):
                    i, j = s.find(c), s.rfind(c)
                    maxL = max(maxL, 1 if i==j else 2+f(s[i+1:j]))
                d[s] = maxL
            return d[s]
        return f(s)
```
