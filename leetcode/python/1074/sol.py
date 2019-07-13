In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1074.number-of-submatrices-that-sum-to-target.algorithms.json

[Java/C++/Python] Find the Subarray with Target Sum

https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/discuss/303750

* Lang:    python
* Author:  lee215
* Votes:   40

[Screenshot](https://www.youtube.com/watch?v=fqoHZmRBpC8)
Leetcode has internal error,
so I cut the screenshot when I finish this one and didn\'t continue.

## **Intuition**
For each row, calculate the prefix sum.
For each pair of columns,
calculate the accumulated sum of rows.
Now this problem is same to, "Find the Subarray with Target Sum".
<br>

## **Complexity**
Time O(N^3), Space O(N)
<br>

**Java**
```
    public int numSubmatrixSumTarget(int[][] A, int target) {
        int m = A.length, n = A[0].length;
        for (int i = 0; i < m; i++)
            for (int j = 1; j < n; j++)
                A[i][j] += A[i][j - 1];
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                Map<Integer, Integer> counter = new HashMap<>();
                counter.put(0, 1);
                int cur = 0;
                for (int k = 0; k < m; k++) {
                    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
                    res += counter.getOrDefault(cur - target, 0);
                    counter.put(cur, counter.getOrDefault(cur, 0) + 1);
                }
            }
        }
        return res;
    }
```

**C++**
```
    int numSubmatrixSumTarget(vector<vector<int>>& A, int target) {
        int m = A.size(), n = A[0].size();
        for (int i = 0; i < m; i++)
            for (int j = 1; j < n; j++)
                A[i][j] += A[i][j - 1];
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                unordered_map<int, int> counter;
                counter[0] = 1;
                int cur = 0;
                for (int k = 0; k < m; k++) {
                    cur += A[k][j] - (i > 0 ? A[k][i - 1] : 0);
                    res += counter[cur - target];
                    counter[cur]++;
                }
            }
        }
        return res;
    }
```

**Python:**
```
        m, n = len(A), len(A[0])
        for row in A:
            for i in xrange(n - 1):
                row[i + 1] += row[i]
        res = 0
        for i in xrange(n):
            for j in xrange(i, n):
                c = collections.Counter({0: 1})
                cur = 0
                for k in xrange(m):
                    cur += A[k][j] - (A[k][i - 1] if i > 0 else 0)
                    res += c[cur - target]
                    c[cur] += 1
        return res
```

