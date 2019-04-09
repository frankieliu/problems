#
# @lc app=leetcode id=255 lang=python3
#
# [255] Verify Preorder Sequence in Binary Search Tree
#
# https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/description/
#
# algorithms
# Medium (43.00%)
# Total Accepted:    33.6K
# Total Submissions: 78.1K
# Testcase Example:  '[5,2,6,1,3]'
#
# Given an array of numbers, verify whether it is the correct preorder
# traversal sequence of a binary search tree.
# 
# You may assume each number in the sequence is unique.
# 
# Consider the following binary search tree: 
# 
# 
# ⁠    5
# ⁠   / \
# ⁠  2   6
# ⁠ / \
# ⁠1   3
# 
# Example 1:
# 
# 
# Input: [5,2,6,1,3]
# Output: false
# 
# Example 2:
# 
# 
# Input: [5,2,1,3,6]
# Output: true
# 
# Follow up:
# Could you do it using only constant space complexity?
# 
#
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        
