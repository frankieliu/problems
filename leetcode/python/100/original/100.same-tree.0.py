#
# @lc app=leetcode id=100 lang=python3
#
# [100] Same Tree
#
# https://leetcode.com/problems/same-tree/description/
#
# algorithms
# Easy (49.21%)
# Total Accepted:    340.8K
# Total Submissions: 692.5K
# Testcase Example:  '[1,2,3]\n[1,2,3]'
#
# Given two binary trees, write a function to check if they are the same or
# not.
# 
# Two binary trees are considered the same if they are structurally identical
# and the nodes have the same value.
# 
# Example 1:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   3     2   3
# 
# ⁠       [1,2,3],   [1,2,3]
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:     1         1
# ⁠         /           \
# ⁠        2             2
# 
# ⁠       [1,2],     [1,null,2]
# 
# Output: false
# 
# 
# Example 3:
# 
# 
# Input:     1         1
# ⁠         / \       / \
# ⁠        2   1     1   2
# 
# ⁠       [1,2,1],   [1,1,2]
# 
# Output: false
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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        
