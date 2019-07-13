#
# @lc app=leetcode id=224 lang=python3
#
# [224] Basic Calculator
#
# https://leetcode.com/problems/basic-calculator/description/
#
# algorithms
# Hard (31.41%)
# Total Accepted:    92.5K
# Total Submissions: 294.3K
# Testcase Example:  '"1 + 1"'
#
# Implement a basic calculator to evaluate a simple expression string.
#
# The expression string may contain open ( and closing parentheses ), the plus
# + or minus sign -, non-negative integers and empty spaces  .
#
# Example 1:
#
#
# Input: "1 + 1"
# Output: 2
#
#
# Example 2:
#
#
# Input: " 2-1 + 2 "
# Output: 3
#
# Example 3:
#
#
# Input: "(1+(4+5+2)-3)+(6+8)"
# Output: 23
# Note:
#
#
# You may assume that the given expression is always valid.
# Do not use the eval built-in library function.
#
#
#
class Solution:
    def calculate(self, ss):
        """
        :type s: str
        :rtype: int
        """

        context = [1]
        sign = 1
        num = 0
        result = 0
        for s in ss:
            if s.isdigit():
                num = num*10 + int(s)
                # print(num)
            if s in ['-', '+']:
                result += sign * num
                sign = context[-1] * [-1, 1][s == '+']
                num = 0
                # print(s, result)
            if s == '(':
                context.append(sign)
                # print(s)
            if s == ')':
                context.pop()
                # print(s)
        result += sign * num
        return result


test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        Input = "(1+(4+5+2)-3)+(6+8)"
        print(s.calculate(Input))
    if case[1]:
        print(s.calculate())
