#
# @lc app=leetcode id=151 lang=python
#
# [151] Reverse Words in a String
#
# https://leetcode.com/problems/reverse-words-in-a-string/description/
#
# algorithms
# Medium (15.83%)
# Total Accepted:    251.3K
# Total Submissions: 1.6M
# Testcase Example:  '"the sky is blue"'
#
# Given an input string, reverse the string word by word.
#
# Example:  
#
#
# Input: "the sky is blue",
# Output: "blue is sky the".
#
#
# Note:
#
#
# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed
# string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the
# reversed string.
#
#
# Follow up: For C programmers, try to solve it in-place in O(1) space.
#
#
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = s.split()
        return " ".join(reversed(a))


test = False
if test:
    s = Solution()
    print(s.reverseWords("the sky is blue"))
