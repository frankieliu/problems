#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#
# https://leetcode.com/problems/triangle/description/
#
# algorithms
# Medium (38.01%)
# Total Accepted:    165.8K
# Total Submissions: 436.2K
# Testcase Example:  '[[2],[3,4],[6,5,7],[4,1,8,3]]'
#
# Given a triangle, find the minimum path sum from top to bottom. Each step you
# may move to adjacent numbers on the row below.
#
# For example, given the following triangle
#
#
# [
# ⁠    [2],
# ⁠   [3,4],
# ⁠  [6,5,7],
# ⁠ [4,1,8,3]
# ]
#
#
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
#
# Bonus point if you are able to do this using only O(n) extra space, where n
# is the total number of rows in the triangle.
#
#
class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        nr = len(triangle)
        if len == 0:
            return 0
        if len == 1:
            return triangle[0][0]
        dp = [0] * nr
        for i in range(0, nr):
            dp[i] = [0] * (i+1)
        dp[nr-1] = triangle[nr-1]
        for i in range(nr-2, -1, -1):
            for j in range(0, i+1):
                dp[i][j] = (min(dp[i+1][j], dp[i+1][j+1]) +
                            triangle[i][j])
        return dp[0][0]


test = False
if test:
    s = Solution()

    # [
    # ⁠    [2],
    # ⁠   [3,4],
    # ⁠  [6,5,7],
    # ⁠ [4,1,8,3]
    # ]
    # [
    # ⁠    [11],
    # ⁠   [9,10],
    # ⁠  [7,6,10],
    # ⁠ [4,1,8,3]
    # ]
    #
    # Note that every level, you loose one of the numbers
    print(s.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]]))
