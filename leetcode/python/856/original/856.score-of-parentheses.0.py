#
# @lc app=leetcode id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.com/problems/score-of-parentheses/description/
#
# algorithms
# Medium (54.94%)
# Total Accepted:    13.8K
# Total Submissions: 25.2K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string S, compute the score of the string based
# on the following rule:
# 
# 
# () has score 1
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: "()"
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: "(())"
# Output: 2
# 
# 
# 
# Example 3:
# 
# 
# Input: "()()"
# Output: 2
# 
# 
# 
# Example 4:
# 
# 
# Input: "(()(()))"
# Output: 6
# 
# 
# 
# 
# Note:
# 
# 
# S is a balanced parentheses string, containing only ( and ).
# 2 <= S.length <= 50
# 
# 
# 
# 
# 
# 
#
class Solution:
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        
