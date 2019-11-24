#
# @lc app=leetcode id=678 lang=python3
#
# [678] Valid Parenthesis String
#
# https://leetcode.com/problems/valid-parenthesis-string/description/
#
# algorithms
# Medium (31.57%)
# Total Accepted:    22.1K
# Total Submissions: 69.9K
# Testcase Example:  '"()"'
#
#
# Given a string containing only three types of characters: '(', ')' and '*',
# write a function to check whether this string is valid. We define the
# validity of a string by these rules:
#
# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left
# parenthesis '(' or an empty string.
# An empty string is also valid.
#
#
#
# Example 1:
#
# Input: "()"
# Output: True
#
#
#
# Example 2:
#
# Input: "(*)"
# Output: True
#
#
#
# Example 3:
#
# Input: "(*))"
# Output: True
#
#
#
# Note:
#
# The string size will be in the range [1, 100].
#
#
#
class Solution:
    def checkValidString(self, s):
        count = [0]
        for el in s:
            if el == '(':
                count = [x+1 for x in count]
            elif el == ')':
                count = [x-1 for x in count]
            else:
                count = list(set([x+1 for x in count] + [x-1 for x in count] + count))
            if all([x < 0 for x in count]):
                return False
            # print(count)
        if any([x ==0 for x in count]):
            return True
        return False



test = True
if test:
    sol = Solution()
    case = [False]*2 + [True] + [False]*3
    if case[0]:
        # Example 1:
        Input = "()"
        # Output: True
        print(sol.checkValidString(Input))
    if case[1]:
        # Example 2:
        Input = "(*)"
        # Output: True
        print(sol.checkValidString(Input))
    if case[2]:
        # Example 3:
        Input = "(*))"
        # Output: True
        print(sol.checkValidString(Input))
