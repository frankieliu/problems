#
# @lc app=leetcode id=301 lang=python3
#
# [301] Remove Invalid Parentheses
#
# https://leetcode.com/problems/remove-invalid-parentheses/description/
#
# algorithms
# Hard (38.03%)
# Total Accepted:    104.9K
# Total Submissions: 275.8K
# Testcase Example:  '"()())()"'
#
# Remove the minimum number of invalid parentheses in order to make the input
# string valid. Return all possible results.
#
# Note: The input string may contain letters other than the parentheses ( and
# ).
#
# Example 1:
#
#
# Input: "()())()"
# Output: ["()()()", "(())()"]
#
#
# Example 2:
#
#
# Input: "(a)())()"
# Output: ["(a)()()", "(a())()"]
#
#
# Example 3:
#
#
# Input: ")("
# Output: [""]
#
#
class Solution:

    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def find_dips(s):
            count = 0
            for i, el in enumerate(s):
                if el == "(":
                    count += 1
                elif el == ")":
                    count -= 1
                if count < 0:
                    print("dip @ {}", i)

                    # the only way to resolve a dip is to remove one
                # of the preceeding parentheses


        find_dips(s)


test = True
if test:
    s = Solution()
    # Input = "x("
    Input = "()())()"
    # Input = ")()("
    # Input = "(((k()(("
    # Input = "(())("
    print(s.removeInvalidParentheses(Input))
