#
# @lc app=leetcode id=291 lang=python3
#
# [291] Word Pattern II
#
# https://leetcode.com/problems/word-pattern-ii/description/
#
# algorithms
# Hard (40.30%)
# Total Accepted:    30.9K
# Total Submissions: 76.8K
# Testcase Example:  '"abab"\n"redblueredblue"'
#
# Given a pattern and a string str, find if str follows the same pattern.
# 
# Here follow means a full match, such that there is a bijection between a
# letter in pattern and a non-empty substring in str.
# 
# Example 1:
# 
# 
# Input: pattern = "abab", str = "redblueredblue"
# Output: true
# 
# Example 2:
# 
# 
# Input: pattern = pattern = "aaaa", str = "asdasdasdasd"
# Output: true
# 
# Example 3:
# 
# 
# Input: pattern = "aabb", str = "xyzabcxzyabc"
# Output: false
# 
# 
# Notes:
# You may assume both pattern and str contains only lowercase letters.
# 
#
class Solution:
    def wordPatternMatch(self, pattern: str, str: str) -> bool:
        
