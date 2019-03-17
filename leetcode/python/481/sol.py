
Short and simple python with boolean

https://leetcode.com/problems/magical-string/discuss/96476

* Lang:    python3
* Author:  rtom09
* Votes:   0

```
class Solution(object):
    def magicalString(self, n):
        s = '122'
        idx = 2
        bl = True
        while len(s) <= n:
            if s[idx] == '1':
                s += '1' if bl else '2'
            else:
                s += '11' if bl else '22'
            idx += 1
            if bl:
                bl = False
            else:
                bl = True

        c = collections.Counter(s[:n])
        return c['1']
        
```
