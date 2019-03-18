
Python recursive and iterative solutions.

https://leetcode.com/problems/binary-tree-inorder-traversal/discuss/31381

* Lang:    python3
* Author:  caikehe
* Votes:   111

        
    # recursively
    def inorderTraversal1(self, root):
        res = []
        self.helper(root, res)
        return res
        
    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)
     
    # iteratively       
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right
