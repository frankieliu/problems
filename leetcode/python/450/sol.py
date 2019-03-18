
Bottom-up Recursive Python Solution. O(log(n)) Time.

https://leetcode.com/problems/delete-node-in-a-bst/discuss/93351

* Lang:    python3
* Author:  boy27910231
* Votes:   11

Idea:
1. When found the node, put right child of the node to the right of the right most leaf node of left child. That way the values are still in order.
2. Return the left child of the node(skip root, a.k.a delete it). If the node doesn't have left child, return right child.
3. Otherwise do binary search. If key < root.val, change left child to the returned new root. Do right child if key > root.val.

This solution always runs in O(log(n)) time since when it finds the node to delete, it goes to the right most leaf of the left sub-tree to put right sub-tree of the node there.

```Python
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root: return None
        
        if root.val == key:
            if root.left:
                # Find the right most leaf of the left sub-tree
                left_right_most = root.left
                while left_right_most.right:
                    left_right_most = left_right_most.right
                # Attach right child to the right of that leaf
                left_right_most.right = root.right
                # Return left child instead of root, a.k.a delete root
                return root.left
            else:
                return root.right
        # If left or right child got deleted, the returned root is the child of the deleted node.
        elif root.val > key:
            root.left = self.deleteNode(root.left, key)
        else:
            root.right = self.deleteNode(root.right, key)
            
        return root
```
