#
# @lc app=leetcode id=251 lang=python3
#
# [251] Flatten 2D Vector
#
# https://leetcode.com/problems/flatten-2d-vector/description/
#
# algorithms
# Medium (43.44%)
# Total Accepted:    53.6K
# Total Submissions: 123.5K
# Testcase Example:  '["Vector2D","next","next","next","hasNext","hasNext","next","hasNext"]\n[[[[1,2],[3],[4]]],[null],[null],[null],[null],[null],[null],[null]]'
#
# Design and implement an iterator to flatten a 2d vector. It should support
# the following operations: next and hasNext.
#
#
#
# Example:
#
#
# Vector2D iterator = new Vector2D([[1,2],[3],[4]]);
#
# iterator.next(); // return 1
# iterator.next(); // return 2
# iterator.next(); // return 3
# iterator.hasNext(); // return true
# iterator.hasNext(); // return true
# iterator.next(); // return 4
# iterator.hasNext(); // return false
#
#
#
#
# Notes:
#
#
# Please remember to RESET your class variables declared in Vector2D, as
# static/class variables are persisted across multiple test cases. Please see
# here for more details.
# You may assume that next() call will always be valid, that is, there will be
# at least a next element in the 2d vector when next() is called.
#
#
#
#
# Follow up:
#
# As an added challenge, try to code it using only iterators in C++ or
# iterators in Java.
#
#
class Vector2D:

    def __init__(self, v):
        def gen(v):
            for row in v:
                for col in row:
                    yield col
        self.gen = gen(v)
        self.lookahead = next(self.gen, None)

    def next(self):
        el = self.lookahead
        if self.hasNext():
            self.lookahead = next(self.gen, None)
        return el

    def hasNext(self):
        return self.lookahead is not None


test = True
if test:
    iterator = Vector2D([[1,2],[3],[4]])

    print(iterator.next())     # return 1
    print(iterator.next())     # return 2
    print(iterator.next())     # return 3
    print(iterator.hasNext())  # True
    print(iterator.hasNext())  # True
    print(iterator.next())     # 4
    print(iterator.hasNext())  # False

    print(">> next one")
    iterator = Vector2D([[]])
    print(iterator.hasNext())
