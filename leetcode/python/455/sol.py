
Python concise & efficient solution

https://leetcode.com/problems/assign-cookies/discuss/94002

* Lang:    python3
* Author:  dalwise
* Votes:   4

My solution from the contest:

```
def findContentChildren(self, g, s):
    g.sort()
    s.sort()
    res = 0
    i = 0
    for e in s:
        if i == len(g):
            break
        if e >= g[i]:
            res += 1
            i += 1
    return res
```

O(nlogn) time and O(1) space
