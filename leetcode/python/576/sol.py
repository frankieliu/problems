
Python DP (beat over 95%) Time: O(N*m*n) Space: 2*(m+2)*(n+2)

https://leetcode.com/problems/out-of-boundary-paths/discuss/102978

* Lang:    python3
* Author:  JeremieMelo
* Votes:   0

```
def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """

        dp = [[1] * (n + 2)]        
        for idx in range(m):
            dp.append([1] + [0] * n + [1])
        dp.append([1] * (n + 2))
        for lev in range(0, N):
            new = [[1] * (n + 2)]        
            for idx in range(m):
                new.append([1] + [0] * n + [1])
            new.append([1] * (n + 2))
            for p in range(1, m + 1):
                for q in range(1, n + 1):
                    new[p][q] = dp[p-1][q] + dp[p][q-1] + dp[p][q+1] + dp[p+1][q]
            dp = new
        return (dp[i+1][j+1]) % (10 ** 9 + 7)
```
