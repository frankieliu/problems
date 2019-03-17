#
# @lc app=leetcode id=556 lang=python3
#
# [556] Next Greater Element III
#
# https://leetcode.com/problems/next-greater-element-iii/description/
#
# algorithms
# Medium (29.59%)
# Total Accepted:    22.3K
# Total Submissions: 75.4K
# Testcase Example:  '12'
#
# Given a positive 32-bit integer n, you need to find the smallest 32-bit
# integer which has exactly the same digits existing in the integer n and is
# greater in value than n. If no such positive 32-bit integer exists, you need
# to return -1.
# 
# Example 1:
# 
# 
# Input: 12
# Output: 21
# 
# 
# 
# 
# Example 2:
# 
# 
# Input: 21
# Output: -1
# 
# 
# 
# 
#
class Solution:
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        
