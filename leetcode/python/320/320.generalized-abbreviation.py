#
# @lc app=leetcode id=320 lang=python3
#
# [320] Generalized Abbreviation
#
# https://leetcode.com/problems/generalized-abbreviation/description/
#
# algorithms
# Medium (48.33%)
# Total Accepted:    36.3K
# Total Submissions: 75.2K
# Testcase Example:  '"word"'
#
# Write a function to generate the generalized abbreviations of a word. 
# 
# Note: The order of the output does not matter.
# 
# Example:
# 
# 
# Input: "word"
# Output:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1",
# "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# 
# 
# 
# 
#
class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        
