#
# @lc app=leetcode id=246 lang=python3
#
# [246] Strobogrammatic Number
#
# https://leetcode.com/problems/strobogrammatic-number/description/
#
# algorithms
# Easy (41.84%)
# Total Accepted:    49.1K
# Total Submissions: 117.4K
# Testcase Example:  '"69"'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
# 
# Write a function to determine if a number is strobogrammatic. The number is
# represented as a string.
# 
# Example 1:
# 
# 
# Input:  "69"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input:  "88"
# Output: true
# 
# Example 3:
# 
# 
# Input:  "962"
# Output: false
# 
#
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        
