#
# @lc app=leetcode id=98 lang=python3
#
# [98] Validate Binary Search Tree
#
# https://leetcode.com/problems/validate-binary-search-tree/description/
#
# algorithms
# Medium (25.09%)
# Total Accepted:    344.1K
# Total Submissions: 1.4M
# Testcase Example:  '[2,1,3]'
#
# Given a binary tree, determine if it is a valid binary search tree (BST).
#
# Assume a BST is defined as follows:
#
#
# The left subtree of a node contains only nodes with keys less than the node's
# key.
# The right subtree of a node contains only nodes with keys greater than the
# node's key.
# Both the left and right subtrees must also be binary search trees.
#
#
# Example 1:
#
#
# Input:
# ⁠   2
# ⁠  / \
# ⁠ 1   3
# Output: true
#
#
# Example 2:
#
#
# ⁠   5
# ⁠  / \
# ⁠ 1   4
# / \
# 3   6
# Output: false
# Explanation: The input is: [5,1,4,null,null,3,6]. The root node's
# value
# is 5 but its right child's value is 4.
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True

        left_valid = self.isValidBST(root.left)
        right_valid = self.isValidBST(root.right)
        right_small = (root.right is None or
                       root.val < self.leftMost(root.right))
        left_large = (root.left is None or
                      root.val > self.rightMost(root.left))

        # print(root.val, left_valid, right_valid, right_small, left_large)
        return (
            left_valid and right_valid and
            right_small and left_large
        )

    def rightMost(self, root):
        while root.right is not None:
            root = root.right
        return root.val

    def leftMost(self, root):
        while root.left is not None:
            root = root.left
        return root.val


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    print(s.isValidBST(tn))
