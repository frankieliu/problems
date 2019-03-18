
Python very straight-forward

https://leetcode.com/problems/reverse-string-ii/discuss/100924

* Lang:    python3
* Author:  Ellest
* Votes:   0

```
    def reverseStr(self, s, k):
        if not s: return s
        i, j = 0, k-1
        chars = [c for c in s]
        while i < len(s):
            x, y = i, min(j, len(s)-1)
            while x < y:
                chars[x], chars[y] = chars[y], chars[x]
                x, y = x + 1, y - 1
            i, j = i + 2*k, j + 2*k
        return ''.join(chars)
```
