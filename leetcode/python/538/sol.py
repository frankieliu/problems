
Python recursive boring solution (linear time, and constant space) with simple explanation

https://leetcode.com/problems/convert-bst-to-greater-tree/discuss/100548

* Lang:    python3
* Author:  laser
* Votes:   2

```
    # O(n) (linear) time, and O(1) (constant) (assuming the output does not count) space complexity
    def convertBST(self, root):
        def generate_greater_tree(node):
            if not node: return None
            right = generate_greater_tree(node.right)
            self.sum += node.val
            new_node = TreeNode(self.sum)
            new_node.right = right
            new_node.left = generate_greater_tree(node.left)
            return new_node
        self.sum = 0
        return generate_greater_tree(root)
```
Explanation: General idea is doing a reverse order traversal, and adding to the sum as you go for the creation of the new tree.
