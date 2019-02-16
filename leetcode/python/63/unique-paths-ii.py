"""A robot is located at the top-left corner of a m x n grid (marked
'Start' in the diagram below).

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid (marked
'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique
paths would there be?


An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Accepted
176,543
Submissions
532,551

"""
class Solution:
    def uniquePathsWithObstacles(self, g):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        m = len(g)
        n = len(g[0])
        if g[0][0] == 1 or g[m-1][n-1] == 1:
            return 0

        dp = [0] * (m+1)
        for i in range(0, m+1):
            dp[i] = [0] * (n+1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                elif g[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
            print(dp)
        return dp[0][0]



s = Solution()
print(s.uniquePathsWithObstacles(
    [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]))
