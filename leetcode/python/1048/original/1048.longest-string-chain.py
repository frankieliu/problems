#
# @lc app=leetcode id=1048 lang=python
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (47.24%)
# Total Accepted:    7.1K
# Total Submissions: 15K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
# 
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
# 
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
# 
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
# 
# 
# 
# Example 1:
# 
# 
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
# 
# 
# 
# 
# 
#
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        
