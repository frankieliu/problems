#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (31.74%)
# Total Accepted:    8.4K
# Total Submissions: 26.5K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
# 
# Example 1:
# 
# 
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
# 
# Example 2:
# 
# 
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
# 
# Example 3:
# 
# 
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
# 
# Note: 1 <= N <= 10 ^ 9.
# 
#
class Solution:
    def consecutiveNumbersSum(self, N):
        """
        :type N: int
        :rtype: int
        """
        
