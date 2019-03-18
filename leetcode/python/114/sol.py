
8 lines of python solution (reverse preorder traversal)

https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/37154

* Lang:    python3
* Author:  girikuncoro
* Votes:   41

    def __init__(self):
        self.prev = None
        
    def flatten(self, root):
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        
        root.right = self.prev
        root.left = None
        self.prev = root
