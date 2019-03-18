
Python 3-Line Elegant Recursion

https://leetcode.com/problems/sum-of-left-leaves/discuss/246397

* Lang:    python3
* Author:  joinyoung
* Votes:   0

Use `flag` to indicate if the current `root` is in the left branch.
```
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode, flag=False) -> int:
        if not root: return 0
        if root.left == root.right == None and flag: return root.val
        return self.sumOfLeftLeaves(root.left, True) + self.sumOfLeftLeaves(root.right, False)
```
