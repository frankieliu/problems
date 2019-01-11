"""101. Symmetric Tree
Easy

1731

36

Favorite

Share

Given a binary tree, check whether it is a mirror of itself (ie,
symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3

But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3

Note:

Bonus points if you could solve it both recursively and iteratively.

Accepted
333,485
Submissions
790,853

"""
class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.isSymTrees(root.left, root.right)

    def isSymTrees(self, left, right):
        if left is None and right is None:
            return True
        if (
                (left is None and right is not None) or
                (left is not None and right is None)
        ):
            return False
        return ((left.val == right.val) and
                self.isSymTrees(left.left, right.right) and
                self.isSymTrees(left.right, right.left))
