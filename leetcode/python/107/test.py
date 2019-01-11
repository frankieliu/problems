class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "({} {} {})".format(self.val, self.left, self.right)

btl = __import__("binary-tree-level-order-traversal-ii")

s = btl.Solution()
t = TreeNode(3)
t.left = TreeNode(9)
t.right = TreeNode(20)
t.right.left = TreeNode(15)
t.right.right = TreeNode(7)

print(s.levelOrderBottom(t))
