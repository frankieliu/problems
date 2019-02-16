"""62. Unique Paths
Medium

1204

86

Favorite

Share

A robot is located at the top-left corner of a m x n grid (marked
'Start' in the diagram below).

The robot can only move either down or right at any point in time. The
robot is trying to reach the bottom-right corner of the grid (marked
'Finish' in the diagram below).

How many possible unique paths are there?

Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:

From the top-left corner, there are a total of 3 ways to reach the
bottom-right corner:

1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

Accepted
248,767
Submissions
543,247
"""

class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        if m <= 1 or n <= 1:
            return 1

        dp = [0] * (m+1)
        for i in range(0, m+1):
            dp[i] = [0] * (n+1)

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]


from collections import defaultdict

s = Solution()
print(s.uniquePaths(3, 2))
print(s.uniquePaths(7, 3))
