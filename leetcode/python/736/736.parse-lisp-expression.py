#
# @lc app=leetcode id=736 lang=python3
#
# [736] Parse Lisp Expression
#
# https://leetcode.com/problems/parse-lisp-expression/description/
#
# algorithms
# Hard (42.90%)
# Total Accepted:    4.8K
# Total Submissions: 11.1K
# Testcase Example:  '"(add 1 2)"'
#
#
# You are given a string expression representing a Lisp-like expression to
# return the integer value of.
#
# The syntax for these expressions is given as follows.
#
# An expression is either an integer, a let-expression, an add-expression, a
# mult-expression, or an assigned variable.  Expressions always evaluate to a
# single integer.
#
# (An integer could be positive or negative.)
#
# A let-expression takes the form (let v1 e1 v2 e2 ... vn en expr), where let
# is always the string "let", then there are 1 or more pairs of alternating
# variables and expressions, meaning that the first variable v1 is assigned the
# value of the expression e1, the second variable v2 is assigned the value of
# the expression e2, and so on sequentially; and then the value of this
# let-expression is the value of the expression expr.
#
# An add-expression takes the form (add e1 e2) where add is always the string
# "add", there are always two expressions e1, e2, and this expression evaluates
# to the addition of the evaluation of e1 and the evaluation of e2.
#
# A mult-expression takes the form (mult e1 e2) where mult is always the string
# "mult", there are always two expressions e1, e2, and this expression
# evaluates to the multiplication of the evaluation of e1 and the evaluation of
# e2.
#
# For the purposes of this question, we will use a smaller subset of variable
# names.  A variable starts with a lowercase letter, then zero or more
# lowercase letters or digits.  Additionally for your convenience, the names
# "add", "let", or "mult" are protected and will never be used as variable
# names.
#
# Finally, there is the concept of scope.  When an expression of a variable
# name is evaluated, within the context of that evaluation, the innermost scope
# (in terms of parentheses) is checked first for the value of that variable,
# and then outer scopes are checked sequentially.  It is guaranteed that every
# expression is legal.  Please see the examples for more details on scope.
#
#
# Evaluation Examples:
#
# Input: (add 1 2)
# Output: 3
#
# Input: (mult 3 (add 2 3))
# Output: 15
#
# Input: (let x 2 (mult x 5))
# Output: 10
#
# Input: (let x 2 (mult x (let x 3 y 4 (add x y))))
# Output: 14
# Explanation: In the expression (add x y), when checking for the value of the
# variable x,
# we check from the innermost scope to the outermost in the context of the
# variable we are trying to evaluate.
# Since x = 3 is found first, the value of x is 3.
#
# Input: (let x 3 x 2 x)
# Output: 2
# Explanation: Assignment in let statements is processed sequentially.
#
# Input: (let x 1 y 2 x (add x y) (add x y))
# Output: 5
# Explanation: The first (add x y) evaluates as 3, and is assigned to x.
# The second (add x y) evaluates as 3+2 = 5.
#
# Input: (let x 2 (add (let x 3 (let x 4 x)) x))
# Output: 6
# Explanation: Even though (let x 4 x) has a deeper scope, it is outside the
# context
# of the final x in the add-expression.  That final x will equal 2.
#
# Input: (let a1 3 b2 (add a1 1) b2)
# Output 4
# Explanation: Variable names can contain digits after the first character.
#
#
#
# Note:
# The given string expression is well formatted: There are no leading or
# trailing spaces, there is only a single space separating different components
# of the string, and no space between adjacent parentheses.  The expression is
# guaranteed to be legal and evaluate to an integer.
# The length of expression is at most 2000.  (It is also non-empty, as that
# would not be a legal expression.)
# The answer and all intermediate calculations of that answer are guaranteed to
# fit in a 32-bit integer.
import re

class Number:
    def __init__(self, number):
        self.number = int(number)
    def __repr__(self):
        return str(self.number)
    def eval(self, frame):
        return self.number

class Variable:
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return self.name
    def eval(self, frame):
        return frame[self.name]

class Let():
    def __init__(self, varlist, expr):
        self.varlist = varlist
        self.expr = expr
    def __repr__(self):
        return "(let " + str(self.varlist) + " " + str(self.expr) + ")"
    def eval(self, frame):
        new_frame = dict(frame)
        for v, expr in self.varlist:
            new_frame[v] = expr.eval(new_frame)
        return self.expr.eval(new_frame)

class Add():
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    def __repr__(self):
        return "(add " + str(self.expr1) + " " + str(self.expr2) + ")"
    def eval(self, frame):
        return self.expr1.eval(frame) + self.expr2.eval(frame)

class Mult():
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2
    def __repr__(self):
        return "(mult " + str(self.expr1) + " " + str(self.expr2) + ")"
    def eval(self, frame):
        return self.expr1.eval(frame) * self.expr2.eval(frame)

class Parser():
    def __init__(self, tokens):
        self.tokens = tokens
        self.cursor = 0

    #----------------------------------------------------------------------

    def lookahead(self, offset=0):
        return self.tokens[self.cursor + offset]

    def consume(self):
        res = self.lookahead()
        self.cursor += 1
        return res

    #----------------------------------------------------------------------

    def parse_var_list(self):
        var_list = []
        la1, la2 = self.lookahead(), self.lookahead(1)
        if la1 == "(" or la2 == ")":  # "(" or no following expr
            return var_list
        else:
            return [self.parse_var_pair()] + self.parse_var_list()

    def parse_var_pair(self):        # returns a tuple
        var = self.consume()
        # print("var:{}".format(var))
        expr = self.parse_expr()
        return (var, expr)

    #----------------------------------------------------------------------

    def parse_let(self):
        self.consume()               # "("
        self.consume()               # "let"
        alist = self.parse_var_list()
        aexpr = self.parse_expr()
        self.consume()               # ")"
        return Let(alist, aexpr)

    def parse_add(self):
        self.consume()               # "("
        self.consume()               # "add"
        expr1 = self.parse_expr()
        expr2 = self.parse_expr()
        self.consume()               # ")"
        return Add(expr1, expr2)

    def parse_mult(self):
        self.consume()               # "("
        self.consume()               # "mult"
        expr1 = self.parse_expr()
        expr2 = self.parse_expr()
        self.consume()               # ")"
        return Mult(expr1, expr2)
    #----------------------------------------------------------------------

    def parse_expr(self):
        x0, x1 = self.lookahead(0), self.lookahead(1)
        if x0 == '(':
            if x1 == 'let':
                return self.parse_let()
            elif x1 == 'add':
                return self.parse_add()
            elif x1 == 'mult':
                return self.parse_mult()
            else:
                print("ERROR")
                return None
        elif x0[0].isalpha():
            return Variable(self.consume())
        elif x0[0].isdigit() or x0[0] == '-':
            return Number(self.consume())
        else:
            print("ERROR")
            return None


class Solution:
    # Let's first write out the grammar
    #
    # expr = add | mult | let | var | int
    #
    # int = -?\d+
    # var = [a-z][a-zA-Z0-9]*
    #
    # add  = '(' 'add' expr expr ')'
    # mult = '(' 'mult' expr expr ')'
    # let  = '(' 'let' var-list expr ')'
    # var-pair  = var expr
    # var-list = var-pair var-list | var-pair

    def evaluate(self, expression):
        tokens = re.findall(r'let|add|mult|\(|\)|-?\d+|[a-z][a-z0-9]*', expression)
        p = Parser(tokens)
        return p.parse_expr().eval([])


test = True
if test:
    sol = Solution()
    case = [False]*7 + [True] + [False]*10
    if case[0]:
        Input = '(add 1 2)'
        # Output: 3
        print(sol.evaluate(Input))
    if case[1]:
        Input = '(mult 3 (add 2 3))'
        # Output: 15
        print(sol.evaluate(Input))
    if case[2]:
        Input = '(let x 2 (mult x 5))'
        # Output: 10
        print(sol.evaluate(Input))
    if case[3]:
        Input = '(let x 2 (mult x (let x 3 y 4 (add x y))))'
        # Output: 14
        print(sol.evaluate(Input))
    if case[4]:
        Input = '(let x (add 2 1) y 3 (mult x y))'
        # Output: 9
        print(sol.evaluate(Input))
    if case[5]:
        Input = '(let x 1 y 2 x (add x y) (add x y))'
        # Output: 9
        print(sol.evaluate(Input))
    if case[6]:
        Input = '(let x 7 -12)'
        # Output: -12
        print(sol.evaluate(Input))
    if case[7]:
        Input = '(add 1 2)'
        # Output: 3
        print(sol.evaluate(Input))
