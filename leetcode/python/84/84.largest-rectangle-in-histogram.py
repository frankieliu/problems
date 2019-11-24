#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (29.95%)
# Total Accepted:    154.2K
# Total Submissions: 514.8K
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given n non-negative integers representing the histogram's bar height where
# the width of each bar is 1, find the area of largest rectangle in the
# histogram.
#
#
#
#
# Above is a histogram where width of each bar is 1, given height =
# [2,1,5,6,2,3].
#
#
#
#
# The largest rectangle is shown in the shaded area, which has area = 10
# unit.
#
#
#
# Example:
#
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
#
#
class Solution:
    def largestRectangleArea(self, heights):
        """
           x
          xx
          xx
          xx x
        x xxxx
        xxxxxx

        The biggest trick in this problem are:
        0. Keeping an increasing stack because we can't make any
           decision until a rectangle has a right boundary
        1. Calculating the width requires both a right and a *left*
           boundary
        2. Creating an artificial left boundary at the beginning (-1)

        0. This is simple:

           2 3 4 (5)
           on adding a 5 into the stack, we can't make a decision on 4
           because a rectangle of 4 could become bigger if there is a 6
           after 5, etc

           2 3 4 (3)
           on adding a 3 into the stack, we know that 4 can't make any more
           rectangles of height 4, since 4 is bounded on the right by the (3)
           and on the left because of construction of an increasing stack
        """

        if len(heights) == 0:
            return 0
        if len(heights) == 1:
            return heights[0]
        s = [-1]
        res = 0
        for ih, h in enumerate(heights):
            while s[-1] != -1 and heights[s[-1]] >= h:
                res = max(res, heights[s.pop()] * (ih - s[-1] - 1))
            s.append(ih)
        ih += 1
        while s[-1] != -1:
            res = max(res, heights[s.pop()] * (ih - s[-1] - 1))
        return(res)


test = True
if test:
    sol = Solution()
    case = [False] * 3 + [True] + [False] * 1
    if case[0]:
        # Example:
        Input = [2, 1, 5, 6, 2, 3]
        # Output: 10
        print(sol.largestRectangleArea(Input))
    if case[1]:
        # Example:
        Input = [1, 1]
        # Output: 2
        print(sol.largestRectangleArea(Input))
    if case[2]:
        # Example:
        Input = [2, 1, 2]
        # Output: 3
        print(sol.largestRectangleArea(Input))
    if case[3]:
        # Example:
        Input = [5, 4, 1, 2]
        # Output: 8
        print(sol.largestRectangleArea(Input))
