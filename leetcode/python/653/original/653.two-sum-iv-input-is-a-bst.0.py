#
# @lc app=leetcode id=653 lang=python3
#
# [653] Two Sum IV - Input is a BST
#
# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/description/
#
# algorithms
# Easy (51.57%)
# Total Accepted:    72.1K
# Total Submissions: 139.8K
# Testcase Example:  '[5,3,6,2,4,null,7]\n9'
#
# Given a Binary Search Tree and a target number, return true if there exist
# two elements in the BST such that their sum is equal to the given target.
# 
# Example 1:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 9
# 
# Output: True
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 
# ⁠   5
# ⁠  / \
# ⁠ 3   6
# ⁠/ \   \
# 2   4   7
# 
# Target = 28
# 
# Output: False
# 
# 
# 
# 
#
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        
