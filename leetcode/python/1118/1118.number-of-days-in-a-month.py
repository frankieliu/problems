#
# @lc app=leetcode id=1118 lang=python
#
# [1118] Number of Days in a Month
#
# https://leetcode.com/problems/number-of-days-in-a-month/description/
#
# algorithms
# Easy (57.16%)
# Total Accepted:    2K
# Total Submissions: 3.5K
# Testcase Example:  '1992\n7'
#
# Given a year Y and a month M, return how many days there are in that
# month.
# 
# 
# 
# Example 1:
# 
# 
# Input: Y = 1992, M = 7
# Output: 31
# 
# 
# Example 2:
# 
# 
# Input: Y = 2000, M = 2
# Output: 29
# 
# 
# Example 3:
# 
# 
# Input: Y = 1900, M = 2
# Output: 28
# 
# 
# 
# 
# Note:
# 
# 
# 1583 <= Y <= 2100
# 1 <= M <= 12
# 
# 
#
class Solution(object):
    def numberOfDays(self, Y, M):
        """
        :type Y: int
        :type M: int
        :rtype: int
        """
        
