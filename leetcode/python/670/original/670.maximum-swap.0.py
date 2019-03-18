#
# @lc app=leetcode id=670 lang=python3
#
# [670] Maximum Swap
#
# https://leetcode.com/problems/maximum-swap/description/
#
# algorithms
# Medium (39.17%)
# Total Accepted:    32K
# Total Submissions: 81.8K
# Testcase Example:  '2736'
#
# 
# Given a non-negative integer, you could swap two digits at most once to get
# the maximum valued number. Return the maximum valued number you could get.
# 
# 
# Example 1:
# 
# Input: 2736
# Output: 7236
# Explanation: Swap the number 2 and the number 7.
# 
# 
# 
# Example 2:
# 
# Input: 9973
# Output: 9973
# Explanation: No swap.
# 
# 
# 
# 
# Note:
# 
# The given number is in the range [0, 10^8]
# 
# 
#
class Solution:
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        
