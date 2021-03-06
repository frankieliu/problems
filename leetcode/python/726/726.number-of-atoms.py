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
import collections
import re

class end_token:
    pass

class literal:
    def __init__(self, val):
        self.val = val

class par:
    def __init__(self, val):
        self.val = val

class atom_exp:
    def __init__(self, exp, n):
        self.exp = exp
        self.n = n
    def __repr__(self):
        return "".join([self.exp, str(self.n)])

class par_exp:
    def __init__(self, exp, n):
        self.exp = exp
        self.n = n
    def __repr__(self):
        return ("[" +
                "".join(map(str, self.exp)) +
                "]" + str(self.n))

class parser:
    def __init__(self):
        self.token = None
        self.d = collections.defaultdict(lambda:0)

    def consume(self):
        t = self.token
        self.next()
        return t

    def lookahead(self):
        return self.token

    def expression(self):
        res = []
        while self.lookahead() != end_token:
            t = self.consume()
            if t == '(':
                mid = self.expression()
                n = int(self.consume())
                el = par_exp(mid, n)
            elif t == ')':
                return res
            else:
                n = self.lookahead()
                if n == end_token or not n[0].isdigit():
                    n = 1
                else:
                    n = int(self.consume())
                # print(t,n)
                el = atom_exp(t, n)
            res.append(el)
        return res

    def next(self):
        if self.si == len(self.s):
            self.token = end_token
            return

        _atom, _number, _par = self.s[self.si]
        self.si += 1

        if _atom:
            self.token = _atom
            return
        if _number:
            self.token = _number
            return
        if _par:
            self.token = _par
            return
        self.token = "No match"

    def parse(self, expression):
        self.s = re.findall('([A-Z][a-z]*)|(\d+)|([()])', expression)
        self.si = 0
        self.next()
        return self.expression()

    def eval(self, exp, mult=1):
        if type(exp) == list:
            for el in exp:
                self.eval(el, mult)
        elif type(exp) == atom_exp:
            self.d[exp.exp] += exp.n*mult
        elif type(exp) == par_exp:
            self.eval(exp.exp, exp.n*mult)


class Solution:
    def countOfAtoms(self, formula):
        p = parser()
        p.eval(p.parse(formula))

        def more1(a):
            if a == 1:
                return ""
            else:
                return str(a)

        return "".join([k + more1(p.d[k])
                        for k in sorted(p.d.keys())])


test = True
if test:
    sol = Solution()
    case = [False]*2 + [True] + [False]*3
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
