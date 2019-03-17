
Concise O(n) 6-liner in Python

https://leetcode.com/problems/unique-substrings-in-wraparound-string/discuss/95463

* Lang:    python3
* Author:  o_sharp
* Votes:   7

Record the longest length for the substrings that end with each letter.

Use ```'abcdefghijklmnopqrstuvwxyza\u2019``` to check if two letters are near each other.

```
class Solution(object):
    def findSubstringInWraproundString(self, p):
        p, d, lo = '0'+p, collections.defaultdict(int), 0
        for hi in range(1, len(p)):
            if p[hi-1]+p[hi] not in 'abcdefghijklmnopqrstuvwxyza':
                lo = hi
            d[p[hi]] = max(d[p[hi]], hi+1-lo)
        return sum(d.values())
```
