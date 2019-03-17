
Python 5-Line DP O(N)

https://leetcode.com/problems/distinct-subsequences-ii/discuss/251682

* Lang:    python3
* Author:  joinyoung
* Votes:   0

I just realized the time complexity is O(N), although it looks like O(N^2). For instance, all the \'a\'s divide the string into several segments. For instance, each time when `char == \'a\'`, the summation `sum(dp[:i])` or `sum(dp[ind:i])` just calculates one of the segments. In total, for `\'a\'`, the complexity is O(N). This applies to other characters as well. Therefore, it is an O(N) algorithm.
```
class Solution:
    def distinctSubseqII(self, S: str) -> int:
        dp, mod = [0] * len(S), 10**9 + 7
        for i, char in enumerate(S):
            ind = S.rfind(char, 0, i)
            dp[i] = 1 + sum(dp[:i]) % mod if ind == -1 else sum(dp[ind:i]) % mod
        return sum(dp) % mod
```
