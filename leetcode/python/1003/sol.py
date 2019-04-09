
Simple python solution using stack

https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/discuss/247616

* Lang:    python3
* Author:  jvs
* Votes:   0

```
def isValid(self, S):
        tac = []
        for s in S:
            tac.append(s)
            if len(tac) >= 3 and tac[-3:] == [\'a\', \'b\', \'c\']:
                tac.pop()
                tac.pop()
                tac.pop()
        return len(tac) == 0
```
