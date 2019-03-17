
Simple Python Solution with Explanation

https://leetcode.com/problems/print-binary-tree/discuss/106268

* Lang:    python3
* Author:  csfaze2
* Votes:   0

The matrix will have `h` rows and `2^h - 1` columns. This will be more than enough to print the contents of the tree. Next, given a bound of `i` and `j`, a node can be placed in the middle, which is calculated as `(i + j) / 2`. 

Let's say `k` is equal to `(i + j) / 2` - this means that the left and right subtrees will be placed one row down at `(i + k) / 2` and `(k + j) / 2`, respectively. When recursively traversing the tree, if a node is `None`, then nothing happens.

```
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        h = self.height(root)
        matrix = [['' for n in range((2 ** h) - 1)] for m in range(h)]

        self.place(root, matrix, 0, (2 ** h) - 1, 0)
        
        return matrix
    
    def height(self, node):
        return max(1 + self.height(node.left), 1 + self.height(node.right)) if node else 0
    
    def place(self, node, matrix, i, j, row):
        if node:
            col = (i + j) // 2
            matrix[row][col] = str(node.val)
            self.place(node.left, matrix, i, col, row + 1)
            self.place(node.right, matrix, col + 1, j, row + 1)
```
