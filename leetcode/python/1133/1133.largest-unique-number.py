#
# @lc app=leetcode id=1133 lang=python
#
# [1133] Largest Unique Number
#
# https://leetcode.com/problems/largest-unique-number/description/
#
# algorithms
# Easy (71.76%)
# Total Accepted:    2.1K
# Total Submissions: 3K
# Testcase Example:  '[5,7,3,9,4,9,8,3,1]'
#
# Given an array of integers A, return the largest integer that only occurs
# once.
# 
# If no integer occurs once, return -1.
# 
# 
# 
# Example 1:
# 
# 
# Input: [5,7,3,9,4,9,8,3,1]
# Output: 8
# Explanation: 
# The maximum integer in the array is 9 but it is repeated. The number 8 occurs
# only once, so it's the answer.
# 
# 
# Example 2:
# 
# 
# Input: [9,9,8,8]
# Output: -1
# Explanation: 
# There is no number that occurs only once.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 2000
# 0 <= A[i] <= 1000
# 
# 
#
class Solution(object):
    def largestUniqueNumber(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        
