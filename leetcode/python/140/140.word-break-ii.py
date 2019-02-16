#
# @lc app=leetcode id=140 lang=python3
#
# [140] Word Break II
#
# https://leetcode.com/problems/word-break-ii/description/
#
# algorithms
# Hard (26.44%)
# Total Accepted:    144.2K
# Total Submissions: 545.4K
# Testcase Example:  '"catsanddog"\n["cat","cats","and","sand","dog"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, add spaces in s to construct a sentence where each word is a
# valid dictionary word. Return all such possible sentences.
# 
# Note:
# 
# 
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
# 
# 
# Example 1:
# 
# 
# Input:
# s = "catsanddog"
# wordDict = ["cat", "cats", "and", "sand", "dog"]
# Output:
# [
# "cats and dog",
# "cat sand dog"
# ]
# 
# 
# Example 2:
# 
# 
# Input:
# s = "pineapplepenapple"
# wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
# Output:
# [
# "pine apple pen apple",
# "pineapple pen apple",
# "pine applepen apple"
# ]
# Explanation: Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input:
# s = "catsandog"
# wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output:
# []
# 
#
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        
