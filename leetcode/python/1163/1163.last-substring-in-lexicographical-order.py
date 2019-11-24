#
# @lc app=leetcode id=1163 lang=python
#
# [1163] Last Substring in Lexicographical Order
#
# https://leetcode.com/problems/last-substring-in-lexicographical-order/description/
#
# algorithms
# Hard (29.95%)
# Total Accepted:    4.2K
# Total Submissions: 14.1K
# Testcase Example:  '"abab"\r'
#
# Given a string s, return the last substring of s in lexicographical
# order.
# 
# 
# 
# Example 1:
# 
# 
# Input: "abab"
# Output: "bab"
# Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
# The lexicographically maximum substring is "bab".
# 
# 
# Example 2:
# 
# 
# Input: "leetcode"
# Output: "tcode"
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= s.length <= 4 * 10^5
# s contains only lowercase English letters.
# 
# 
#
class Solution(object):
    def lastSubstring(self, s):
        """
        :type s: str
        :rtype: str
        """
        
