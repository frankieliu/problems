
Concise 6-liner in Python

https://leetcode.com/problems/can-i-win/discuss/95328

* Lang:    python3
* Author:  o_sharp
* Votes:   0

Recursion with memorization:
```
class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        def f(l, target):
            if (tuple(l), target) not in d:
                d[(tuple(l), target)] = any(not f(l[:i]+l[i+1:], target-n) for i,n in enumerate(l)) if max(l)<target else True
            return d[(tuple(l), target)]
        d, l = {}, range(1, maxChoosableInteger+1)
        return False if sum(l) < desiredTotal else f(l, desiredTotal)
```
