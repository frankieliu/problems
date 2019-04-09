#
# @lc app=leetcode id=248 lang=python3
#
# [248] Strobogrammatic Number III
#
# https://leetcode.com/problems/strobogrammatic-number-iii/description/
#
# algorithms
# Hard (35.88%)
# Total Accepted:    18.6K
# Total Submissions: 51.7K
# Testcase Example:  '"50"\n"100"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to count the total strobogrammatic numbers that exist in the
# range of low <= num <= high.
# 
# Example:
# 
# 
# Input: low = "50", high = "100"
# Output: 3 
# Explanation: 69, 88, and 96 are three strobogrammatic numbers.
# 
# Note:
# Because the range might be a large number, the low and high numbers are
# represented as string.
# 
#
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        
