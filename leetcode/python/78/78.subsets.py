#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#
# https://leetcode.com/problems/subsets/description/
#
# algorithms
# Medium (50.31%)
# Total Accepted:    319.8K
# Total Submissions: 635.5K
# Testcase Example:  '[1,2,3]'
#
# Given a set of distinct integers, nums, return all possible subsets (the
# power set).
# 
# Note: The solution set must not contain duplicate subsets.
# 
# Example:
# 
# 
# Input: nums = [1,2,3]
# Output:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
