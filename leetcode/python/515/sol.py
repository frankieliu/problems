
Can my solution be improved upon?

https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/232334

* Lang:    python3
* Author:  anonymous36
* Votes:   0

```
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        
        def levelOrderTraversal(node, depth, lsts):
            if node == None:
                return
            else:
                lsts[depth].append(node.val)
                
                if len(lsts) < (depth+2):
                    lsts += [[]]
                
                levelOrderTraversal(node.left, depth+1, lsts)
                levelOrderTraversal(node.right, depth+1, lsts)
                
        lsts = [[]]
        levelOrderTraversal(root, 0, lsts) if root else None
        res = [max(lst) for lst in lsts if lst != []]
        return res
```

Time-Complexity: O(n) where n is the number of nodes.
Space-Complexity: O(h) where h is the height of the tree.
