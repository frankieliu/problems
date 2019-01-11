"""112. Path Sum
Easy

709

229

Favorite

Share
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:

Given the below binary tree and sum = 22,

      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

Accepted
270,340
Submissions
739,513
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root is None:
            return False
        return self.hasSum(root, sum)

    def hasSum(self, root, sum):
        if root.left is None and root.right is None:
            return root.val == sum

        if root.left is None:
            return self.hasSum(root.right, sum - root.val)

        if root.right is None:
            return self.hasSum(root.left, sum - root.val)

        return (self.hasSum(root.left, sum - root.val) or
                self.hasSum(root.right, sum - root.val))



        )
