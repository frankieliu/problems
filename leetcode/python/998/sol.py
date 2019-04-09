
Python iterative (beats 100%) and recursive solutions

https://leetcode.com/problems/maximum-binary-tree-ii/discuss/257163

* Lang:    python3
* Author:  kiddan
* Votes:   0

Iterative - 
```
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root.val < val:
            node = TreeNode(val)
            node.left = root
            return node
        
        curr = root
        while curr and curr.val > val:
            prev = curr
            curr = curr.right
            
        if not curr:
            prev.right = TreeNode(val)
        else:
            node = TreeNode(val)
            prev.right = node
            node.left = curr
            
        return root
```

Recursive - 
```
class Solution(object):
    def insertIntoMaxTree(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return TreeNode(val)
        
        if val > root.val:
            node = TreeNode(val)
            node.left = root
            return node
        else:
            root.right = self.insertIntoMaxTree(root.right, val)
            return root
```
