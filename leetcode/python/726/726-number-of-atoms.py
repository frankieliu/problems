#
# @lc app=leetcode id=726 lang=python3
#
# [726] Number of Atoms
#
# https://leetcode.com/problems/number-of-atoms/description/
#
# algorithms
# Hard (43.85%)
# Total Accepted:    8.9K
# Total Submissions: 20.3K
# Testcase Example:  '"H2O"'
#
# Given a chemical formula (given as a string), return the count of each atom.
#
# An atomic element always starts with an uppercase character, then zero or
# more lowercase letters, representing the name.
#
# 1 or more digits representing the count of that element may follow if the
# count is greater than 1.  If the count is 1, no digits will follow.  For
# example, H2O and H2O2 are possible, but H1O2 is impossible.
#
# Two formulas concatenated together produce another formula.  For example,
# H2O2He3Mg4 is also a formula.
#
# A formula placed in parentheses, and a count (optionally added) is also a
# formula.  For example, (H2O2) and (H2O2)3 are formulas.
#
# Given a formula, output the count of all elements as a string in the
# following form: the first name (in sorted order), followed by its count (if
# that count is more than 1), followed by the second name (in sorted order),
# followed by its count (if that count is more than 1), and so on.
#
# Example 1:
#
# Input:
# formula = "H2O"
# Output: "H2O"
# Explanation:
# The count of elements are {'H': 2, 'O': 1}.
#
#
#
# Example 2:
#
# Input:
# formula = "Mg(OH)2"
# Output: "H2MgO2"
# Explanation:
# The count of elements are {'H': 2, 'Mg': 1, 'O': 2}.
#
#
#
# Example 3:
#
# Input:
# formula = "K4(ON(SO3)2)2"
# Output: "K4N2O14S4"
# Explanation:
# The count of elements are {'K': 4, 'N': 2, 'O': 14, 'S': 4}.
#
#
#
# Note:
# All atom names consist of lowercase letters, except for the first character
# which is uppercase.
# The length of formula will be in the range [1, 1000].
# formula will only consist of letters, digits, and round parentheses, and is a
# valid formula as defined in the problem.
#
#
import re

class end_token:
    pass

class literal:
    def __init__(self, val):
        self.val = val
    def nud(self):
        return int(self.val)

class atom:
    def __init__(self, exp, val):
        self.val = val
        self.exp = exp
    def nud(self):

    def led(self, val):

class parn

class parser:
    def __init__(self):
        self.token = None

    def consume(self):
        t = self.token
        self.next()
        return t

    def lookahead(self):
        return self.token

    def expression(self):
        left = self.consume().nud()
        while self.lookahead() != end_token:

        return left

    def next(self):
        if self.si == len(self.s):
            self.token = end_token
            return

        _atom, _number, _par = self.s[self.si]
        self.si += 1
        if atom:
            return atom(self.expression, _atom)
        if number:
            return literal(self.expression, _number)
        if paren:
            return par(self.expression)

    def parse(self, expression):
        self.s = re.findall('([A-Z][a-z]*)|(\d+)|([()])', expression)
        self.si = 0
        for i in range(0,10):
            print(self.consume())

class Solution:
    def countOfAtoms(self, formula):
        """
        :type formula: str
        :rtype: str
        """
        p = parser()
        p.parse(formula)


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*3
    if case[0]:
        # Example 1:
        formula = "H2O"
        # Output: "H2O"
        print(sol.countOfAtoms(formula))
    if case[1]:
        # Example 2:
        formula = "Mg(OH)2"
        # Output: "H2MgO2"
        print(sol.countOfAtoms(formula))
    if case[2]:
        # Example 3:
        formula = "K4(ON(SO3)2)2"
        # Output: "K4N2O14S4"
        print(sol.countOfAtoms(formula))
