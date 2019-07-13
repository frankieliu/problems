#
# @lc app=leetcode id=1044 lang=python
#
# [1044] Longest Duplicate Substring
#
# https://leetcode.com/problems/longest-duplicate-substring/description/
#
# algorithms
# Hard (22.78%)
# Total Accepted:    2.1K
# Total Submissions: 9.1K
# Testcase Example:  '"banana"'
#
# Given a string S, consider all duplicated substrings: (contiguous) substrings
# of S that occur 2 or more times.  (The occurrences may overlap.)
# 
# Return any duplicated substring that has the longest possible length.  (If S
# does not have a duplicated substring, the answer is "".)
# 
# 
# 
# Example 1:
# 
# 
# Input: "banana"
# Output: "ana"
# 
# 
# Example 2:
# 
# 
# Input: "abcd"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# 2 <= S.length <= 10^5
# S consists of lowercase English letters.
# 
#
class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        
