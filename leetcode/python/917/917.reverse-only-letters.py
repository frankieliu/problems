#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# https://leetcode.com/problems/reverse-only-letters/description/
#
# algorithms
# Easy (56.03%)
# Total Accepted:    17.2K
# Total Submissions: 30.8K
# Testcase Example:  '"ab-cd"'
#
# Given a string S, return the "reversed" string where all characters that are
# not a letter stay in the same place, and all letters reverse their
# positions.
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
# 
# 
# 
# Example 1:
# 
# 
# Input: "ab-cd"
# Output: "dc-ba"
# 
# 
# 
# Example 2:
# 
# 
# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# 
# 
# 
# Example 3:
# 
# 
# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"
# 
# 
# 
# 
# 
# Note:
# 
# 
# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122 
# S doesn't contain \ or "
# 
# 
# 
# 
# 
#
class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        
