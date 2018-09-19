# find if tree is balanced

class tree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def maxDepth(self):
        l = 0
        if self.left is not None:
            l = self.left.maxDepth()
        r = 0
        if self.right is not None:
            r = self.right.maxDepth()
        return max(l, r) + 1

    def minDepth(self):
        l = 0
        if self.left is not None:
            l = self.left.maxDepth()
        r = 0
        if self.right is not None:
            r = self.right.maxDepth()
        return min(l, r) + 1

    def str(self):
        return str(self.value)

    def balanced(self):
        if (self.maxDepth() - self.minDepth()) <= 1:
            return True
        else:
            return False

    def print(self, indent=0):
        print(" "*indent, self.str())
        if self.left is not None:
            self.left.print(indent+1)
        if self.right is not None:
            self.right.print(indent+1)


t = tree(1,
         tree(2, tree(4, tree(8, tree(10), tree(11)), tree(9)), tree(5)),
         tree(3, tree(6), tree(7)))
t.print()
print(t.balanced())
