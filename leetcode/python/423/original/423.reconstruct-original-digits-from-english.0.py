#
# @lc app=leetcode id=423 lang=python3
#
# [423] Reconstruct Original Digits from English
#
# https://leetcode.com/problems/reconstruct-original-digits-from-english/description/
#
# algorithms
# Medium (45.32%)
# Total Accepted:    17.8K
# Total Submissions: 39.4K
# Testcase Example:  '"owoztneoer"'
#
# Given a non-empty string containing an out-of-order English representation of
# digits 0-9, output the digits in ascending order.
# 
# Note:
# 
# Input contains only lowercase English letters.
# Input is guaranteed to be valid and can be transformed to its original
# digits. That means invalid inputs such as "abc" or "zerone" are not
# permitted.
# Input length is less than 50,000.
# 
# 
# 
# Example 1:
# 
# Input: "owoztneoer"
# 
# Output: "012"
# 
# 
# 
# Example 2:
# 
# Input: "fviefuro"
# 
# Output: "45"
# 
# 
#
class Solution:
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        
