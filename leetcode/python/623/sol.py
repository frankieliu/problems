
Can my solution be improved? [Python]

https://leetcode.com/problems/add-one-row-to-tree/discuss/232356

* Lang:    python3
* Author:  anonymous36
* Votes:   0

```
class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        
        def addLevel(node, depth):
            if node == None:
                return
            else:
                if depth + 1 == d:
                    left = node.left
                    node.left = TreeNode(v)
                    node.left.left = left
                        
                    
                    right = node.right
                    node.right = TreeNode(v)
                    node.right.right = right
                else:
                    addLevel(node.left, depth+1)
                    addLevel(node.right, depth+1)
                    
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            addLevel(root, 1)
            return root
```

Time-Complexity: O(n) where n is the number of nodes.
Space-Complexity: O(h) where h is the height of three.
