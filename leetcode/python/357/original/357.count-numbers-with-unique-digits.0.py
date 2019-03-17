#
# @lc app=leetcode id=357 lang=python3
#
# [357] Count Numbers with Unique Digits
#
# https://leetcode.com/problems/count-numbers-with-unique-digits/description/
#
# algorithms
# Medium (46.51%)
# Total Accepted:    57.6K
# Total Submissions: 123.8K
# Testcase Example:  '2'
#
# Given a non-negative integer n, count all numbers with unique digits, x,
# where 0 ≤ x < 10^n.
# 
# 
# Example:
# 
# 
# Input: 2
# Output: 91 
# Explanation: The answer should be the total numbers in the range of 0 ≤ x <
# 100, 
# excluding 11,22,33,44,55,66,77,88,99
# 
# 
#
class Solution:
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
