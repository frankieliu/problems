#
# @lc app=leetcode id=267 lang=python3
#
# [267] Palindrome Permutation II
#
# https://leetcode.com/problems/palindrome-permutation-ii/description/
#
# algorithms
# Medium (33.28%)
# Total Accepted:    24.8K
# Total Submissions: 74.4K
# Testcase Example:  '"aabb"'
#
# Given a string s, return all the palindromic permutations (without
# duplicates) of it. Return an empty list if no palindromic permutation could
# be form.
# 
# Example 1:
# 
# 
# Input: "aabb"
# Output: ["abba", "baab"]
# 
# Example 2:
# 
# 
# Input: "abc"
# Output: []
# 
#
class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        
