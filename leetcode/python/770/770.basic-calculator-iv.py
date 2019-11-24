#
# @lc app=leetcode id=770 lang=python3
#
# [770] Basic Calculator IV
#
# https://leetcode.com/problems/basic-calculator-iv/description/
#
# algorithms
# Hard (44.32%)
# Total Accepted:    1.7K
# Total Submissions: 3.7K
# Testcase Example:  '"e + 8 - a + 5"\n["e"]\n[1]'
#
# Given an expression such as expression = "e + 8 - a + 5" and an evaluation
# map such as {"e": 1} (given in terms of evalvars = ["e"] and evalints = [1]),
# return a list of tokens representing the simplified expression, such as
# ["-1*a","14"]
#
#
# An expression alternates chunks and symbols, with a space separating each
# chunk and symbol.
# A chunk is either an expression in parentheses, a variable, or a non-negative
# integer.
# A variable is a string of lowercase letters (not including digits.) Note that
# variables can be multiple letters, and note that variables never have a
# leading coefficient or unary operator like "2x" or "-x".
#
#
# Expressions are evaluated in the usual order: brackets first, then
# multiplication, then addition and subtraction. For example, expression = "1 +
# 2 * 3" has an answer of ["7"].
#
# The format of the output is as follows:
#
#
# For each term of free variables with non-zero coefficient, we write the free
# variables within a term in sorted order lexicographically. For example, we
# would never write a term like "b*a*c", only "a*b*c".
# Terms have degree equal to the number of free variables being multiplied,
# counting multiplicity. (For example, "a*a*b*c" has degree 4.) We write the
# largest degree terms of our answer first, breaking ties by lexicographic
# order ignoring the leading coefficient of the term.
# The leading coefficient of the term is placed directly to the left with an
# asterisk separating it from the variables (if they exist.)  A leading
# coefficient of 1 is still printed.
# An example of a well formatted answer is ["-2*a*a*a", "3*a*a*b", "3*b*b",
# "4*a", "5*c", "-6"]
# Terms (including constant terms) with coefficient 0 are not included.  For
# example, an expression of "0" has an output of [].
#
#
# Examples:
#
#
# Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
# Output: ["-1*a","14"]
#
# Input: expression = "e - 8 + temperature - pressure",
# evalvars = ["e", "temperature"], evalints = [1, 12]
# Output: ["-1*pressure","5"]
#
# Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
# Output: ["1*e*e","-64"]
#
# Input: expression = "7 - 7", evalvars = [], evalints = []
# Output: []
#
# Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
# Output: ["5*a*b*c"]
#
# Input: expression = "((a - b) * (b - c) + (c - a)) * ((a - b) + (b - c) * (c
# - a))",
# evalvars = [], evalints = []
# Output:
# ["-1*a*a*b*b","2*a*a*b*c","-1*a*a*c*c","1*a*b*b*b","-1*a*b*b*c","-1*a*b*c*c","1*a*c*c*c","-1*b*b*b*c","2*b*b*c*c","-1*b*c*c*c","2*a*a*b","-2*a*a*c","-2*a*b*b","2*a*c*c","1*b*b*b","-1*b*b*c","1*b*c*c","-1*c*c*c","-1*a*a","1*a*b","1*a*c","-1*b*c"]
#
#
# Note:
#
#
# expression will have length in range [1, 250].
# evalvars, evalints will have equal lengths in range [0, 100].
#
#
#
import re
"""

The problem with infix is that you can't make a decision
until you know the surrounding operators.  For example:

  op1 1 op2
      ^

  1. first read token at 1 (literal)
  2. then read the next operator (op2)
  3. at this point you can decide whether op1 should operate on
     a. 1, or
     b. (1 op2 ...)
  4. if op1 is more strongly binding (or has a higher priority) than op2,
     it will take precedence and it will follow 3.a.
  5. if op2 is more strongly binding, then we begin evaluating an expression
     beginning at 1 and continuing to the right


Pratt parser uses the following variables to denote the binding power:

  rbp       lbp
   -->     <--
   ^    1    +

The right binding power and left binding power, and if left binding
power is greater than right binding power then I go left :)

Why is it called lbp?  Because each infix operator takes operands from
both its left and right sides.  For the operator + on the right hand side
we care about its left binding power, since we care how strongly it binds
to its left operand, 1 in this case.

So what happens in this case?  We insert ^ for $ for logical beginning and
end points of the expression, with low binding powers (0).

^ 1 + 2 + 3 $

The first + has larger left binding power than the "beginning
expression(^)"'s right binding power, therefore it is going to call
+'s led() function.  led() is short for left denotation but I will
call it left-do, that is it takes a left and looks for a right
operand to combine with it.  We end up with

(1+2) + 3 + 4

where (1+2) is the new left.  Note that led() actually calls upon
expression() to right the right operand.  In this case it passes
to expression its right binding power (10) when looking for the
expression on the right.

Expression needs this rbp, because it needs to determine what the
infix operator '+' should combine with.  The operator's rbp is passed
to expression(), so that expression will look for an expression that
terminating before an operator with the same or lower binding power.

Why? Because an operator on the right with a lower lbp should not
take precedence over the current operator.

In this case, when the next expression takes '2' it stops at '2' after
taking a look the following +'s lbp.  Since the next operator's lbp is
the same as the current operator's rbp, the first operator should take
precedence because it came first (the usual convention).  Pictorially,


           current     next      next
          operator     token     operator
                 v       v       v
                 +       2       +
                 -->           <--
                 rbp           lpb


   expression() returns 2 because the current operator takes
   precedence over the following operator which has the same
   binding power.


At this point left-do (led) of the first + combines its left and right
and returns a new left, i.e. replace 1 with 1+2,

1st left: 1
2nd left: 1+2

But note that we are still within the first expression() beginning with
the first literal which came with a low right binding power of the
beginning of expression 'operator' (rbp = 0).

This means that we take the next + (the one following 2) and compare
its lbp with the rbp of ^, and since the next +'s lbp is greater than
^'s rbp it combines the new left with the next right expression
beginning at 3 (which evaluates to a 3, we will explain shortly), i.e.

(1+2) : new left

gets combined via second's + led() function which finds the next right
expression

3

and the new left after the combination looks like

((1+2)+3)

Note again the right expression() is called by the second +'s led()
function.  expression() ends at 3, because the second +'s rbp is
greater than the end expression's left binding power ($'s rbp is set
to 0).

Finally this generates new left in the top level expression() call.  The
next operator's that it sees is the end expression token ($), which has
the same binding power as the begin expression token (^).   Both have a
binding power of 0 and the top level expression() exits with the left
it has computed thus far, returning

((1+2)+3)

"""
import collections
class poly(collections.Counter):
    """
    to add two polynomials, need to figure out
    """
    def __add__(self, other):
        self.update(other)
        return self
    def __sub__(self, other):
        self.update({k: -v for k,v in other.items()})
        return self
    def __mult__(self, other):
        ans = Poly()
        for k1, v1 in self.items():
            for k2, v2 in other.items():
                ans.update({tuple(sorted(k1+k2)): v1*v2})
        return ans



class var:
    def __init__(self, name):
        self.val = name

    def nud(self):
        return self.val

    def __repr__(self):
        return str(self.val)


class literal:
    def __init__(self, num):
        self.val = num

    def nud(self):
        return self.val

    def __repr__(self):
        return str(self.val)


class infix:
    def __init__(self, exp, id, lbp):
        self.exp = exp
        self.id = id
        self.lbp = lbp
        self.left = ""
        self.right = ""

    def nud(self):
        # used for prefix -
        # this has a strong left right binding power
        self.left = 0
        self.right = self.exp(100)
        return self

    def led(self, left):
        self.left = left
        self.right = self.exp(self.lbp)
        return self

    def __repr__(self):
        return "(" + " ".join([self.id, str(self.left), str(self.right)]) + ")"


class left_paren:
    def __init__(self, exp, consume):
        self.lbp = 0
        self.exp = exp
        self.consume = consume

    def nud(self):
        res = self.exp(self.lbp)
        if type(self.consume()) != right_paren:
            print("Error expecting a right parentheses")
        return res

    def __repr__(self):
        return "("


class right_paren:
    lbp = 0

    def __repr__(self):
        return ")"


class end_token:
    def __init__(self):
        self.lbp = 0

    def __repr__(self):
        return "end_token"


class parser:
    def __init__(self):
        self.op_map = {
            '+': (lambda: infix(self.expression, '+', 10)),
            '-': (lambda: infix(self.expression, '-', 10)),
            '*': (lambda: infix(self.expression, '*', 50)),
            '(': (lambda: left_paren(self.expression, self.consume)),
            ')': (lambda: right_paren())
        }
        self.token = None
        pass

    def consume(self):
        t = self.token
        self.next()
        return t

    def lookahead(self):
        return self.token

    def expression(self, rbp=0):
        left = self.consume().nud()
        while rbp < self.lookahead().lbp:  # if the next op has higher priority
            t = self.consume()
            left = t.led(left)
        print(left)
        return left

    def parse(self, program):
        exp = program.replace(" ", "")  # get rid of extra spaces
        rg = re.compile('(\d+)|([-()+*])|([a-z]+)')

        self.symbols = rg.findall(exp)
        self.symboli = 0
        print(self.symbols)
        self.next()
        return self.expression(0)

        # print("num:{} op:{} name:{}".format(num,op,name))
        # return expression()

    def next(self):
        if self.symboli == len(self.symbols):
            self.token = end_token()
            return
        num, op, name = self.symbols[self.symboli]
        print("num:{} op:{} name:{}".format(num, op, name))
        self.symboli += 1
        if num:
            self.token = literal(num)
            return
        if op:
            self.token = self.op_map[op]()
            return
        if name:
            self.token = var(name)
            return
        self.token = "error"


class Solution:
    def basicCalculatorIV(self, expression, evalvars, evalints):
        """
        let's write a EBNF
        expr: var | int | add | mult | sub
        add: expr '+' expr
        sub: expr '-' expr
        mul: expr '*' expr
        """
        p = parser()
        p.parse(expression)


test = True
if test:
    sol = Solution()
    case = [False] * 0 + [True] + [False] * 1
    if case[0]:
        # Examples:
        example = "-e + -8 * (0 - a + 5)"
        evalvars = ["e"]
        evalints = [1]
        # Output: ["-1*a","14"]
        print(sol.basicCalculatorIV(example, evalvars, evalints))
