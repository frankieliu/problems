#
# @lc app=leetcode id=1119 lang=python
#
# [1119] Remove Vowels from a String
#
# https://leetcode.com/problems/remove-vowels-from-a-string/description/
#
# algorithms
# Easy (89.37%)
# Total Accepted:    4.8K
# Total Submissions: 5.3K
# Testcase Example:  '"leetcodeisacommunityforcoders"'
#
# Given a string S, remove the vowels 'a', 'e', 'i', 'o', and 'u' from it, and
# return the new string.
# 
# 
# 
# Example 1:
# 
# 
# Input: "leetcodeisacommunityforcoders"
# Output: "ltcdscmmntyfrcdrs"
# 
# 
# Example 2:
# 
# 
# Input: "aeiou"
# Output: ""
# 
# 
# 
# 
# Note:
# 
# 
# S consists of lowercase English letters only.
# 1 <= S.length <= 1000
# 
# 
#
class Solution(object):
    def removeVowels(self, S):
        """
        :type S: str
        :rtype: str
        """
        
