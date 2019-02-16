#
# @lc app=leetcode id=16 lang=python3
#
# [16] 3Sum Closest
#
# https://leetcode.com/problems/3sum-closest/description/
#
# algorithms
# Medium (33.80%)
# Total Accepted:    232.4K
# Total Submissions: 687.5K
# Testcase Example:  '[-1,2,1,-4]\n1'
#
# Given an array nums of n integers and an integer target, find three integers
# in nums such that the sum is closest to target. Return the sum of the three
# integers. You may assume that each input would have exactly one solution.
# 
# Example:
# 
# 
# Given array nums = [-1, 2, 1, -4], and target = 1.
# 
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# 
# 
#
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
