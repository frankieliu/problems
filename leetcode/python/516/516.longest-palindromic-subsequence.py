#
# @lc app=leetcode id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.com/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (44.97%)
# Total Accepted:    50.1K
# Total Submissions: 111.3K
# Testcase Example:  '"bbbab"'
#
# 
# Given a string s, find the longest palindromic subsequence's length in s. You
# may assume that the maximum length of s is 1000.
# 
# 
# Example 1:
# Input: 
# 
# "bbbab"
# 
# Output: 
# 
# 4
# 
# One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# Input:
# 
# "cbbd"
# 
# Output:
# 
# 2
# 
# One possible longest palindromic subsequence is "bb".
# 
#
class Solution:
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        
