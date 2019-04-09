#
# @lc app=leetcode id=625 lang=python3
#
# [625] Minimum Factorization
#
# https://leetcode.com/problems/minimum-factorization/description/
#
# algorithms
# Medium (31.73%)
# Total Accepted:    6.1K
# Total Submissions: 19.2K
# Testcase Example:  '48'
#
# Given a positive integer a, find the smallest positive integer b whose
# multiplication of each digit equals to a. 
# 
# 
# If there is no answer or the answer is not fit in 32-bit signed integer, then
# return 0.
# 
# 
# Example 1
# Input:
# 48 
# Output:
# 68
# 
# 
# 
# Example 2
# Input: 
# 15
# 
# Output:
# 35
# 
#
class Solution:
    def smallestFactorization(self, a: int) -> int:
        
