
Python solution. Concise (3 lines) & efficient (O(n^2))

https://leetcode.com/problems/4sum-ii/discuss/93977

* Lang:    python3
* Author:  dalwise
* Votes:   0

My solution from the contest:
```
def fourSumCount(self, A, B, C, D):
    n = len(A)
    s = collections.Counter(-A[a]-B[b] for a in range(n) for b in range(n))
    return sum(s[C[c]+D[d]] for c in range(n) for d in range(n))
```
