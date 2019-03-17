
4 lines in Python

https://leetcode.com/problems/word-break/discuss/43788

* Lang:    python3
* Author:  StefanPochmann
* Votes:   91

`ok[i]` tells whether `s[:i]` can be built.

    def wordBreak(self, s, words):
        ok = [True]
        for i in range(1, len(s)+1):
            ok += any(ok[j] and s[j:i] in words for j in range(i)),
        return ok[-1]
