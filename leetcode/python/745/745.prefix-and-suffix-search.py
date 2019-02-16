#
# @lc app=leetcode id=745 lang=python3
#
# [745] Prefix and Suffix Search
#
# https://leetcode.com/problems/prefix-and-suffix-search/description/
#
# algorithms
# Hard (28.89%)
# Total Accepted:    10.5K
# Total Submissions: 36.3K
# Testcase Example:  '["WordFilter","f"]\n[[["apple"]], ["a","e"]]'
#
# 
# Given many words, words[i] has weight i.
# 
# Design a class WordFilter that supports one function, WordFilter.f(String
# prefix, String suffix).
# It will return the word with given prefix and suffix with maximum weight.  If
# no word exists, return -1.
# 
# 
# Examples:
# 
# Input:
# WordFilter(["apple"])
# WordFilter.f("a", "e") // returns 0
# WordFilter.f("b", "") // returns -1
# 
# 
# Note:
# 
# words has length in range [1, 15000].
# For each test case, up to words.length queries WordFilter.f may be made.
# words[i] has length in range [1, 10].
# prefix, suffix have lengths in range [0, 10].
# words[i] and prefix, suffix queries consist of lowercase letters only.
# 
# 
#
class WordFilter:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        

    def f(self, prefix, suffix):
        """
        :type prefix: str
        :type suffix: str
        :rtype: int
        """
        


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
