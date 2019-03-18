#
# @lc app=leetcode id=940 lang=python3
#
# [940] Distinct Subsequences II
#
# https://leetcode.com/problems/distinct-subsequences-ii/description/
#
# algorithms
# Hard (36.88%)
# Total Accepted:    3.7K
# Total Submissions: 9.9K
# Testcase Example:  '"abc"'
#
# Given a string S, count the number of distinct, non-empty subsequences of S
# .
# 
# Since the result may be large, return the answer modulo 10^9 + 7.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abc"
# Output: 7
# Explanation: The 7 distinct subsequences are "a", "b", "c", "ab", "ac", "bc",
# and "abc".
# 
# 
# 
# Example 2:
# 
# 
# Input: "aba"
# Output: 6
# Explanation: The 6 distinct subsequences are "a", "b", "ab", "ba", "aa" and
# "aba".
# 
# 
# 
# Example 3:
# 
# 
# Input: "aaa"
# Output: 3
# Explanation: The 3 distinct subsequences are "a", "aa" and "aaa".
# 
# 
# 
# 
# 
# 
# 
# 
# Note:
# 
# 
# S contains only lowercase letters.
# 1 <= S.length <= 2000
# 
# 
# 
# 
# 
# 
# 
# 
# 
#
class Solution:
    def distinctSubseqII(self, S):
        """
        :type S: str
        :rtype: int
        """
        
