#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (33.56%)
# Total Accepted:    59.3K
# Total Submissions: 176.7K
# Testcase Example:  '"aba"'
#
# 
# Given a non-empty string s, you may delete at most one character.  Judge
# whether you can make it a palindrome.
# 
# 
# Example 1:
# 
# Input: "aba"
# Output: True
# 
# 
# 
# Example 2:
# 
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# 
# 
# Note:
# 
# The string will only contain lowercase characters a-z.
# The maximum length of the string is 50000.
# 
# 
#
class Solution:
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
