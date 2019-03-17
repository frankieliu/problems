
Python-two pointer solution, beat 100% in speed

https://leetcode.com/problems/long-pressed-name/discuss/244893

* Lang:    python3
* Author:  zhohu
* Votes:   0

```
class Solution(object):
    def isLongPressedName(self, name, typed):
        i, j = 0,0
        if len(typed) < len(name):
            return False
        elif typed == name:
            return True
        
        while i <= len(name) - 1:
            if name[i] == typed[j]:
                j += 1
                i += 1
                
            else:
                j += 1
            if j == len(typed) and i != len(name):
                return False
        return True
```
