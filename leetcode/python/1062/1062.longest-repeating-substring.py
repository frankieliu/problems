#
# @lc app=leetcode id=1062 lang=python
#
# [1062] Longest Repeating Substring
#
# https://leetcode.com/problems/longest-repeating-substring/description/
#
# algorithms
# Medium (51.39%)
# Total Accepted:    738
# Total Submissions: 1.4K
# Testcase Example:  '"abcd"'
#
# Given a string S, find out the length of the longest repeating substring(s).
# Return 0 if no repeating substring exists.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abcd"
# Output: 0
# Explanation: There is no repeating substring.
# 
# 
# Example 2:
# 
# 
# Input: "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of
# which occurs twice.
# 
# 
# Example 3:
# 
# 
# Input: "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3
# times.
# 
# 
# Example 4:
# 
# 
# Input: "aaaaa"
# Output: 4
# Explanation: The longest repeating substring is "aaaa", which occurs
# twice.
# 
# 
# 
# 
# Note:
# 
# 
# The string S consists of only lowercase English letters from 'a' - 'z'.
# 1 <= S.length <= 1500
# 
#
class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        
