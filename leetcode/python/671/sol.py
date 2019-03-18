
Python iterative

https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/discuss/107160

* Lang:    python3
* Author:  zhe22
* Votes:   0

```
class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        cand = None
        
        walk = root
        stack =[]
        prev = None
        
        while walk or stack:
            if walk:
                # print(walk.val)
                if walk.val > root.val:
                    if cand is None or cand > walk.val:
                        cand = walk.val
                    walk = None # no need to check the sub tree of walk, all >= walk.val
                else: # ==
                    stack.append(walk)
                    walk = walk.left
            else:
                node = stack.pop()
                
                # Only check the right child when a possible result exists
                if (node.right and prev is not node.right) and (cand is None or node.right.val < cand):
                    walk = node.right
                    stack.append(node)
                else:
                    prev = node
        
        return cand or -1
```
