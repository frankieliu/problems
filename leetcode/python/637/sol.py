
A pythonic BFS solution

https://leetcode.com/problems/average-of-levels-in-binary-tree/discuss/105122

* Lang:    python3
* Author:  JieMei
* Votes:   1

```
class Solution(object):
    def averageOfLevels(self, root):
        ans = []
        lvl = [root]
        while lvl:
            ans.append(sum(n.val for n in lvl) / float(len(lvl)))
            lvl = [c for n in lvl for c in [n.left, n.right] if c]
        return ans
```
