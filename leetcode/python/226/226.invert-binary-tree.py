#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
# https://leetcode.com/problems/invert-binary-tree/description/
#
# algorithms
# Easy (56.63%)
# Total Accepted:    292.3K
# Total Submissions: 516.1K
# Testcase Example:  '[4,2,7,1,3,6,9]'
#
# Invert a binary tree.
# 
# Example:
# 
# Input:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 2     7
# ⁠/ \   / \
# 1   3 6   9
# 
# Output:
# 
# 
# ⁠    4
# ⁠  /   \
# ⁠ 7     2
# ⁠/ \   / \
# 9   6 3   1
# 
# Trivia:
# This problem was inspired by this original tweet by Max Howell:
# 
# Google: 90% of our engineers use the software you wrote (Homebrew), but you
# can’t invert a binary tree on a whiteboard so f*** off.
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
