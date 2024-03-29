#
# @lc app=leetcode id=549 lang=python3
#
# [549] Binary Tree Longest Consecutive Sequence II
#
# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/
#
# algorithms
# Medium (44.06%)
# Total Accepted:    15.5K
# Total Submissions: 35.2K
# Testcase Example:  '[1,2,3,4]'
#
# Given a binary tree, you need to find the length of Longest Consecutive Path
# in Binary Tree.
# 
# Especially, this path can be either increasing or decreasing. For example,
# [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is
# not valid. On the other hand, the path can be in the child-Parent-child
# order, where not necessarily be parent-child order.
# 
# Example 1:
# 
# 
# Input:
# ⁠       1
# ⁠      / \
# ⁠     2   3
# Output: 2
# Explanation: The longest consecutive path is [1, 2] or [2, 1].
# 
# 
# 
# 
# Example 2:
# 
# 
# Input:
# ⁠       2
# ⁠      / \
# ⁠     1   3
# Output: 3
# Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
# 
# 
# 
# 
# Note: All the values of tree nodes are in the range of [-1e7, 1e7].
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        
