#
# @lc app=leetcode id=243 lang=python3
#
# [243] Shortest Word Distance
#
# https://leetcode.com/problems/shortest-word-distance/description/
#
# algorithms
# Easy (56.38%)
# Total Accepted:    60.5K
# Total Submissions: 107.3K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"coding"\n"practice"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
# 
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
# 
# 
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
# 
# 
# 
# Input: word1 = "makes", word2 = "coding"
# Output: 1
# 
# 
# Note:
# You may assume that word1 does not equal to word2, and word1 and word2 are
# both in the list.
# 
#
class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
