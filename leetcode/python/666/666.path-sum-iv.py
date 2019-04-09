#
# @lc app=leetcode id=666 lang=python3
#
# [666] Path Sum IV
#
# https://leetcode.com/problems/path-sum-iv/description/
#
# algorithms
# Medium (51.53%)
# Total Accepted:    7.6K
# Total Submissions: 14.8K
# Testcase Example:  '[113,215,221]'
#
# 
# If the depth of a tree is smaller than 5, then this tree can be represented
# by a list of three-digits integers.
# 
# 
# 
# For each integer in this list:
# 
# The hundreds digit represents the depth D of this node, 1 
# The tens digit represents the position P of this node in the level it belongs
# to, 1 . The position is the same as that in a full binary tree. 
# The units digit represents the value V of this node, 0 
# 
# 
# 
# 
# Given a list of ascending three-digits integers representing a binary with
# the depth smaller than 5. You need to return the sum of all paths from the
# root towards the leaves.
# 
# 
# Example 1:
# 
# Input: [113, 215, 221]
# Output: 12
# Explanation: 
# The tree that the list represents is:
# ⁠   3
# ⁠  / \
# ⁠ 5   1
# 
# The path sum is (3 + 5) + (3 + 1) = 12.
# 
# 
# 
# Example 2:
# 
# Input: [113, 221]
# Output: 4
# Explanation: 
# The tree that the list represents is: 
# ⁠   3
# ⁠    \
# ⁠     1
# 
# The path sum is (3 + 1) = 4.
# 
# 
#
class Solution:
    def pathSum(self, nums: List[int]) -> int:
        
