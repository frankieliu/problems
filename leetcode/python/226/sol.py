
3-4 lines Python

https://leetcode.com/problems/invert-binary-tree/discuss/62714

* Lang:    python3
* Author:  StefanPochmann
* Votes:   90

    def invertTree(self, root):
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

Maybe make it four lines for better readability:

    def invertTree(self, root):
        if root:
            invert = self.invertTree
            root.left, root.right = invert(root.right), invert(root.left)
            return root

---

And an iterative version using my own stack:

    def invertTree(self, root):
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                node.left, node.right = node.right, node.left
                stack += node.left, node.right
        return root
