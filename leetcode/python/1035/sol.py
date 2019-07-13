In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1035.uncrossed-lines.algorithms.json

[Java/C++/Python] DP, The Longest Common Subsequence

https://leetcode.com/problems/uncrossed-lines/discuss/282842

* Lang:    python
* Author:  lee215
* Votes:   41

## Solution 1: Straight Forward 2D DP
Time `O(N^2)`, Space `O(N^2)`

**Java:**
```
    public int maxUncrossedLines(int[] A, int[] B) {
        int m = A.length, n = B.length, dp[][] = new int[m + 1][n + 1];
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                if (A[i - 1] == B[j - 1])
                    dp[i][j] = 1 + dp[i - 1][j - 1];
                else
                    dp[i][j] = Math.max(dp[i][j - 1], dp[i - 1][j]);
        return dp[m][n];
    }
```

**C++:**
```
    int maxUncrossedLines(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size(), dp[m+1][n+1];
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= m; ++i)
            for (int j = 1; j <= n; ++j)
                dp[i][j] = A[i - 1] == B[j - 1] ? dp[i - 1][j - 1] + 1 : max(dp[i][j - 1], dp[i - 1][j]);
        return dp[m][n];
    }
```

**Python:**
```
    def maxUncrossedLines(self, A, B):
        dp, m, n = collections.defaultdict(int), len(A), len(B)
        for i in xrange(m):
            for j in xrange(n):
                dp[i, j] = max(dp[i - 1, j - 1] + (A[i] == B[j]), dp[i - 1, j], dp[i, j - 1])
        return dp[m - 1, n - 1]
```


## Solution 2: 1D DP
Time `O(N^2)`, Space `O(N)`
**Python:**
```
    def maxUncrossedLines(self, A, B):
        m, n = len(A), len(B)
        dp = [0] * (n + 1)
        for i in xrange(m):
            for j in range(n)[::-1]:
                if A[i] == B[j]: dp[j + 1] = dp[j] + 1
            for j in range(n):
                dp[j + 1] = max(dp[j + 1], dp[j])
        return dp[n]
```
