"""64. Minimum Path Sum
Medium

1070

27

Favorite

Share

Given a m x n grid filled with non-negative numbers, find a path from
top left to bottom right which minimizes the sum of all numbers along
its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
Accepted
201,180
Submissions
447,545

"""

import sys
class Solution:
    def minPathSum(self, g):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(g)
        if m == 0:
            return 0
        n = len(g[0])
        if m == 1 and n == 1:
            return g[0][0]

        dp = [0]*(m+1)
        for i in range(0, m+1):
            dp[i] = [sys.maxsize]*(n+1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = g[i][j]
                    continue
                dp[i][j] = min(dp[i+1][j], dp[i][j+1]) + g[i][j]
        return dp[0][0]


s = Solution()
print(s.minPathSum(
    [
        [1, 3, 1],
        [1, 5, 1],
        [4, 2, 1]
    ]
))
