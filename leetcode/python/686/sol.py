
Python straight-forward binary search solution

https://leetcode.com/problems/repeated-string-match/discuss/108105

* Lang:    python3
* Author:  sparklethinker
* Votes:   0

The idea is to search the minimum number of times `A` has to be repeated within a lower bound and an upper bound using binary search. The lower bound is 1 while the upper bound is `len(B) / len(A) + 1` if B is longer than A or `len(A) / len(B) + 1` otherwise.
```
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if len(A) == 0:
            return -1
        nrep = len(B) / len(A) + 1 if len(B) >= len(A) else len(A) / len(B) + 1
        s = A * nrep
        lo = 1
        hi = nrep
        minrep = nrep
        flag = False
        while lo <= hi:
            mid = lo + (hi - lo) / 2
            if B in s[0:mid*len(A)]:
                flag = True
                minrep = min(minrep, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return minrep if flag else -1
```
