#
# @lc app=leetcode id=424 lang=python3
#
# [424] Longest Repeating Character Replacement
#
# https://leetcode.com/problems/longest-repeating-character-replacement/description/
#
# algorithms
# Medium (43.42%)
# Total Accepted:    26.1K
# Total Submissions: 60.2K
# Testcase Example:  '"ABAB"\n2'
#
# Given a string that consists of only uppercase English letters, you can
# replace any letter in the string with another letter at most k times. Find
# the length of a longest substring containing all repeating letters you can
# get after performing the above operations.
#
# Note:
# Both the string's length and k will not exceed 10^4.
#
#
#
# Example 1:
#
# Input:
# s = "ABAB", k = 2
#
# Output:
# 4
#
# Explanation:
# Replace the two 'A's with two 'B's or vice versa.
#
#
#
#
# Example 2:
#
# Input:
# s = "AABABBA", k = 1
#
# Output:
# 4
#
# Explanation:
# Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
#
#
#
from collections import defaultdict

class Solution:
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        count = defaultdict(lambda: 0)
        for char in s:
            count[char] += 1
        for k, v in count.items():
            print(k, v)


test = True
if test:
    s = Solution()
    print(s.characterReplacement("aaabbbccc", 1))
