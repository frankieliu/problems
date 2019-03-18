
Python Solution, Tree Traversal

https://leetcode.com/problems/construct-string-from-binary-tree/discuss/104037

* Lang:    python3
* Author:  yang_fan
* Votes:   0

Just follow [shawngao's clear solution](https://discuss.leetcode.com/topic/91308/java-solution-tree-traversal).
```
def tree2str(self, t):
        if not t:return ''
        res=str(t.val)+''
        left=self.tree2str(t.left)
        right=self.tree2str(t.right)
        if not left and not right: return res
        if not left: return res+'()'+'('+right+')'
        if not right: return res+'('+left+')'
        return res+'('+left+')'+'('+right+')'
```
