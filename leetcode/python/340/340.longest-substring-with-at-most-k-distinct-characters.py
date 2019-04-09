#
# @lc app=leetcode id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Hard (39.23%)
# Total Accepted:    67.8K
# Total Submissions: 172.9K
# Testcase Example:  '"eceba"\n2'
#
# Given a string, find the length of the longest substring T that contains at
# most k distinct characters.
# 
# Example 1:
# 
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: T is "aa" which its length is 2.
# 
# 
# 
#
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
