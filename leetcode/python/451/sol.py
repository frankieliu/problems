
1-liner in Python. Concise and efficient.

https://leetcode.com/problems/sort-characters-by-frequency/discuss/93548

* Lang:    python3
* Author:  o_sharp
* Votes:   1

This gives me 49ms that beats 99%.
```
class Solution(object):
    def frequencySort(self, s):
        return ''.join(c*s.count(c) for c in sorted(set(s), key=s.count)[::-1])
```

The counter solution is slower and longer.
```
class Solution(object):
    def frequencySort(self, s):
        cnt = collections.Counter(s)
        return ''.join(c*cnt[c] for c in sorted(set(s),key=cnt.get)[::-1])
```
