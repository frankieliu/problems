#
# @lc app=leetcode id=241 lang=python3
#
# [241] Different Ways to Add Parentheses
#
# https://leetcode.com/problems/different-ways-to-add-parentheses/description/
#
# algorithms
# Medium (48.59%)
# Total Accepted:    67.3K
# Total Submissions: 138.5K
# Testcase Example:  '"2-1-1"'
#
# Given a string of numbers and operators, return all possible results from
# computing all the different possible ways to group numbers and operators. The
# valid operators are +, - and *.
#
# Example 1:
#
#
# Input: "2-1-1"
# Output: [0, 2]
# Explanation:
# ((2-1)-1) = 0
# (2-(1-1)) = 2
#
# Example 2:
#
#
# Input: "2*3-4*5"
# Output: [-34, -14, -10, -10, 10]
# Explanation:
# (2*(3-(4*5))) = -34
# ((2*3)-(4*5)) = -14
# ((2*(3-4))*5) = -10
# (2*((3-4)*5)) = -10
# (((2*3)-4)*5) = 10
#
#
import re
from itertools import product


class Solution:
    """
    Consider the different pairing:

    a op b op c op d

    Essentially there are three ops and you need to
    choose the order of these operations

    let's call the ops x, y, z

    x y z
    1 2 3
    1 3 2
    2 1 3
    2 3 1
    3 1 2
    3 2 1

    Seems like there are 6 possible pairings
    then why there are only 5 choices?

    In this case if y is the last operation, then

    x y z
    1 3 2
    2 3 1

    are equivalent, can we extend this idea to larger
    groupings?

    w x y z
    1 2 3 4

    if y is the last operation, then you can sort of
    do the operation wx and z in somewhat interleave
    fashion and not change the result

    """
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operands = [int(x) for x in re.split('[+\-*]', input)]
        ops = [map_op(x) for x in re.split('\d+', input)[1:-1]]
        return self._diff(operands, ops)

    def _diff(self, operands, ops):
        if len(ops) == 0:
            return [operands[0]]
        if len(ops) == 1:
            return [ops[0](*operands)]
        out = []
        for el in range(len(ops)):
            print(el,operands[0:el+1], ops[0:el])
            print(el,operands[el+1:], ops[el+1:])
            out += product(self._diff(operands[0:el+1], ops[0:el]),
                           self._diff(operands[el+1:], ops[el:]))
        return out


def map_op(op):
    h = {}
    h['+'] = add
    h['-'] = sub
    h['*'] = mult
    return h[op]


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def mult(x, y):
    return x*y


test = True
if test:
    s = Solution()
    Input = "2*3-4*5"
    # Input = "2*3"
    print(s.diffWaysToCompute(Input))
    print(map_op('+')(2, 3))
