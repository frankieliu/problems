In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1043.partition-array-for-maximum-sum.algorithms.json

[Java/C++/Python] DP

https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863

* Lang:    python
* Author:  lee215
* Votes:   61

## **Explanation**

`dp[i]` record the maximum sum we can get considering `A[0] ~ A[i]`
To get `dp[i]`, we will try to change `k` last numbers separately to the maximum of them,
where `k = 1` to `k = K`.

## **Complexity**
Time `O(NK)`, Space `O(N)`

<br>

**Java:**
```
    public int maxSumAfterPartitioning(int[] A, int K) {
        int N = A.length, dp[] = new int[N];
        for (int i = 0; i < N; ++i) {
            int curMax = 0;
            for (int k = 1; k <= K && i - k + 1 >= 0; ++k) {
                curMax = Math.max(curMax, A[i - k + 1]);
                dp[i] = Math.max(dp[i], (i >= k ? dp[i - k] : 0) + curMax * k);
            }
        }
        return dp[N - 1];
    }
```

**C++:**
```
    int maxSumAfterPartitioning(vector<int>& A, int K) {
        int N = A.size();
        vector<int> dp(N);
        for (int i = 0; i < N; ++i) {
            int curMax = 0;
            for (int k = 1; k <= K && i - k + 1 >= 0; ++k) {
                curMax = max(curMax, A[i - k + 1]);
                dp[i] = max(dp[i], (i >= k ? dp[i - k] : 0) + curMax * k);
            }
        }
        return dp[N - 1];
    }
```

**Python:**
```
    def maxSumAfterPartitioning(self, A, K):
        N = len(A)
        dp = [0] * (N + 1)
        for i in xrange(N):
            curMax = 0
            for k in xrange(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                dp[i] = max(dp[i], dp[i - k] + curMax * k)
        return dp[N - 1]
```

