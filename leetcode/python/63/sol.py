
Python different solutions (O(m*n), O(n), in place).

https://leetcode.com/problems/unique-paths-ii/discuss/23410

* Lang:    python3
* Author:  caikehe
* Votes:   20

        
    # O(m*n) space
    def uniquePathsWithObstacles1(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in xrange(c)] for _ in xrange(r)]
        dp[0][0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, r):
            dp[i][0] = dp[i-1][0] * (1 - obstacleGrid[i][0])
        for i in xrange(1, c):
            dp[0][i] = dp[0][i-1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            for j in xrange(1, c):
                dp[i][j] = (dp[i][j-1] + dp[i-1][j]) * (1 - obstacleGrid[i][j])
        return dp[-1][-1]
        
    # O(n) space
    def uniquePathsWithObstacles2(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        cur = [0] * c
        cur[0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, c):
            cur[i] = cur[i-1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            cur[0] *= (1 - obstacleGrid[i][0])
            for j in xrange(1, c):
                cur[j] = (cur[j-1] + cur[j]) * (1 - obstacleGrid[i][j])
        return cur[-1]
    
    # in place
    def uniquePathsWithObstacles(self, obstacleGrid):
        if not obstacleGrid:
            return 
        r, c = len(obstacleGrid), len(obstacleGrid[0])
        obstacleGrid[0][0] = 1 - obstacleGrid[0][0]
        for i in xrange(1, r):
            obstacleGrid[i][0] = obstacleGrid[i-1][0] * (1 - obstacleGrid[i][0])
        for i in xrange(1, c):
            obstacleGrid[0][i] = obstacleGrid[0][i-1] * (1 - obstacleGrid[0][i])
        for i in xrange(1, r):
            for j in xrange(1, c):
                obstacleGrid[i][j] = (obstacleGrid[i-1][j] + obstacleGrid[i][j-1]) * (1 - obstacleGrid[i][j])
        return obstacleGrid[-1][-1]
