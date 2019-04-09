#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (47.95%)
# Total Accepted:    35.5K
# Total Submissions: 74K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
# 
# A Uni-value subtree means all nodes of the subtree have the same value.
# 
# Example :
# 
# 
# Input:  root = [5,1,5,5,5,null,5]
# 
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
# 
# Output: 4
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
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        
