#
# @lc app=leetcode id=1153 lang=python
#
# [1153] String Transforms Into Another String
#
# https://leetcode.com/problems/string-transforms-into-another-string/description/
#
# algorithms
# Hard (28.08%)
# Total Accepted:    1.3K
# Total Submissions: 4.4K
# Testcase Example:  '"aabcc"\n"ccdee"'
#
# Given two strings str1 and str2 of the same length, determine whether you can
# transform str1 into str2 by doing zero or more conversions.
# 
# In one conversion you can convert all occurrences of one character in str1 to
# any other lowercase English character.
# 
# Return true if and only if you can transform str1 into str2.
# 
# 
# 
# Example 1:
# 
# 
# Input: str1 = "aabcc", str2 = "ccdee"
# Output: true
# Explanation: Convert 'c' to 'e' then 'b' to 'd' then 'a' to 'c'. Note that
# the order of conversions matter.
# 
# 
# Example 2:
# 
# 
# Input: str1 = "leetcode", str2 = "codeleet"
# Output: false
# Explanation: There is no way to transform str1 to str2.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= str1.length == str2.length <= 10^4
# Both str1 and str2 contain only lowercase English letters.
# 
# 
#
class Solution(object):
    def canConvert(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: bool
        """
        
