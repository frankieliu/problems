
[Python] dp, 16 lines

https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/247528

* Lang:    python3
* Author:  cc189
* Votes:   4

```python
class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        INF = float(\'inf\')
        dp = [ [ [ INF for i in range(n+1)] for i in range(n+1) ] for i in range(n+1) ]
        prefix_sum = [0 for i in range(n + 1)]
        for i in range(1, n + 1): prefix_sum[i] = prefix_sum[i - 1] + stones[i - 1]
        for i in range(1, n + 1): dp[i][i][1] = 0
        for tail in range(1, n + 1):
            for i in range(1, n - tail + 2):
                j = i + tail - 1
                for size in range(2, tail + 1):
                    for t in range(i, j):
                        dp[i][j][size] = min(dp[i][j][size], dp[i][t][size - 1] + dp[t + 1][j][1])
                    dp[i][j][1] = min(dp[i][j][1], dp[i][j][k] + prefix_sum[j] - prefix_sum[i - 1])
        return -1 if dp[1][n][1] == INF else dp[1][n][1]
```
