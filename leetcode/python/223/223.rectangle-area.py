#
# @lc app=leetcode id=223 lang=python3
#
# [223] Rectangle Area
#
# https://leetcode.com/problems/rectangle-area/description/
#
# algorithms
# Medium (35.41%)
# Total Accepted:    82.6K
# Total Submissions: 233.4K
# Testcase Example:  '-3\n0\n3\n4\n0\n-1\n9\n2'
#
# Find the total area covered by two rectilinear rectangles in a 2D plane.
#
# Each rectangle is defined by its bottom left corner and top right corner as
# shown in the figure.
#
#
#
# Example:
#
#
# Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
# Output: 45
#
# Note:
#
# Assume that the total area is never beyond the maximum possible value of int.
#
#
class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # (A,B) (C,D)
        # (E,F) (G,H)

        a1 = (C-A)*(D-B)
        a2 = (G-E)*(H-F)

        # Find the two inner points:
        x = inter1D([A, C], [E, G])
        y = inter1D([B, D], [F, H])
        inter = (x[1]-x[0]) * (y[1]-y[0])
        return a1 + a2 - inter


def inter1D(int1, int2):
    int1, int2 = sorted([int1, int2])
    # print(int1, int2)
    if int2[0] < int1[1]:  # intersection
        return [int2[0], min(int1[1], int2[1])]
    else:
        return [0, 0]


test = True
if test:
    # Input:
    A = -3
    B = 0
    C = 3
    D = 4
    E = 0
    F = -1
    G = 9
    H = 2
    # Output: 45
    s = Solution()
    print(s.computeArea(A, B, C, D, E, F, G, H))
