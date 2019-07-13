#
# @lc app=leetcode id=149 lang=python3
#
# [149] Max Points on a Line
#
# https://leetcode.com/problems/max-points-on-a-line/description/
#
# algorithms
# Hard (15.49%)
# Total Accepted:    110.6K
# Total Submissions: 714.5K
# Testcase Example:  '[[1,1],[2,2],[3,3]]'
#
# Given n points on a 2D plane, find the maximum number of points that lie on
# the same straight line.
#
# Example 1:
#
#
# Input: [[1,1],[2,2],[3,3]]
# Output: 3
# Explanation:
# ^
# |
# |        o
# |     o
# |  o  
# +------------->
# 0  1  2  3  4
#
#
# Example 2:
#
#
# Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4
# Explanation:
# ^
# |
# |  o
# |     o        o
# |        o
# |  o        o
# +------------------->
# 0  1  2  3  4  5  6
#
#
#
# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

from collections import defaultdict, Counter

class Solution:
    def maxPoints(self, points):
        """

        Key point: a point and a slope define a line

        \forall a \in points

           reset count and overlap

           \forall b \in other points

              generate rational slope from a to b : p/q
                either
                   overlap++      if no defined slope
                   count[p/q]++   otherwise

           update global max ( count + overlap + 1(self) )


        Note: special case: when points overlap, there is no defined slope,
              use 0/0 to indicate no well defined slope

        """

        if len(points) <= 1:
            return len(points)

        def gcd(a,b):
            if b == 0:
                return a
            return gcd(b, a%b)

        def get_slope(p1, p2):
            if p1[0] == p2[0] and p1[1] == p2[1]:
                return (0,0)
            if p1[0] == p2[0]:
                return (1,0)
            if p1[1] == p2[1]:
                return (0,1)
            dx = p2[0] - p1[0]
            dy = p2[1] - p1[1]
            g = gcd(dx, dy)
            return (dy/g, dx/g)

        m = 0
        for i in range(0, len(points)-1):
            count = defaultdict(lambda:0)
            overlap = 0
            for j in range(i+1, len(points)):
                slope = get_slope(points[i], points[j])
                if slope == (0,0):
                    overlap += 1
                else:
                    count[slope] += 1
            m = max(m, max(count.values(), default=0) + 1 + overlap)
        return m


test = True
if test:
    s = Solution()
    case = [False]*2 + [True] + [False]*2
    if case[0]:
        # Example 1:
        Input = [[1,1],[2,2],[3,3]]
        # Output: 3
        print(s.maxPoints(Input))
    if case[1]:
        # Example 2:
        Input = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
        # Output: 4
        print(s.maxPoints(Input))
    if case[2]:
        # Example 2:
        Input = [[0,0],[0,0]]
        # Output: 2
        print(s.maxPoints(Input))
    if case[3]:
        # Example 2:
        Input = [[0,0],[1,1],[0,0]]
        # Output: 3
        print(s.maxPoints(Input))
