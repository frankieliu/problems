
Easy Recursive Python 7 lines Solution

https://leetcode.com/problems/path-sum-iii/discuss/91942

* Lang:    python3
* Author:  YJL1228
* Votes:   14

Similar to #112 and #113, check the whole tree.
The only difference is: Any node can play as start or end in a valid path.
After each visit, use current node as start, and update the "targets" list.
Pass the updated targets and initial target through.

Base case:
1. node is None

Recursive case:
1. node fits in certain path sum.
2. node doesn't meet.

```
class Solution(object):
    def pathSum(self, root, s):
        return self.helper(root, s, [s])

    def helper(self, node, origin, targets):
        if not node: return 0
        hit = 0
        for t in targets:
            if not t-node.val: hit += 1                          # count if sum == target
        targets = [t-node.val for t in targets]+[origin]         # update the targets
        return hit+self.helper(node.left, origin, targets)+self.helper(node.right, origin, targets)
```
