
O(n) python beats 95%

https://leetcode.com/problems/is-subsequence/discuss/87261

* Lang:    python3
* Author:  Mrcommon_zzzzzz
* Votes:   0

"""
def isSubsequence(self, s, t):
        for e in s:
            if e not in t:
                return False
            t = t[t.index(e)+1:]
        return True
"""
