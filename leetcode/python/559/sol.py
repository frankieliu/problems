
Can someone explain what's really wrong with this Python code?

https://leetcode.com/problems/maximum-depth-of-n-ary-tree/discuss/251750

* Lang:    python3
* Author:  Ashutoshkumar
* Votes:   0

Can someone explain what\'s really wrong with this code?
```
class Solution:
    h = 1
    def maxDepth(self, root: \'Node\') -> int:
        # print(root.val, self.h)
        if root is None:
            return 0
        for ch in root.children:
            # print(ch.val)
            self.h = max(self.h, self.maxDepth(ch))
        return self.h
```
