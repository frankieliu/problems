In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1031.maximum-sum-of-two-non-overlapping-subarrays.algorithms.json

[Java/C++/Python] O(N)Time O(1) Space

https://leetcode.com/problems/maximum-sum-of-two-non-overlapping-subarrays/discuss/278251

* Lang:    python
* Author:  lee215
* Votes:   98

## **Explanation**

`Lsum`, sum of the last `L` elements
`Msum`, sum of the last `M` elements

`Lmax`, max sum of contiguous `L` elements before the last `M` elements.
`Mmax`, max sum of contiguous `M` elements before the last `L` elements/


## **Complexity**
Two pass, `O(N)` time,
`O(1)` extra space.

It can be done in one pass. I just don\'t feel like merging them.
If you don\'t like change the original input, don\'t have to.

<br>

**Java:**
```
    public int maxSumTwoNoOverlap(int[] A, int L, int M) {
        for (int i = 1; i < A.length; ++i)
            A[i] += A[i - 1];
        int res = A[L + M - 1], Lmax = A[L - 1], Mmax = A[M - 1];
        for (int i = L + M; i < A.length; ++i) {
            Lmax = Math.max(Lmax, A[i - M] - A[i - L - M]);
            Mmax = Math.max(Mmax, A[i - L] - A[i - L - M]);
            res = Math.max(res, Math.max(Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]));
        }
        return res;
    }
```

**Another Java**
```
    public int maxSumTwoNoOverlap(int[] A, int L, int M) {
        int res = 0, Lsum = 0, Lmax = 0, Msum = 0, Mmax = 0;
        for (int i = 0; i < A.length; ++i) {
            Msum += A[i];
            if (i - M >= 0) Msum -= A[i - M];
            if (i - M >= 0) Lsum += A[i - M];
            if (i - M - L >= 0) Lsum -= A[i - L - M];
            Lmax = Math.max(Lmax, Lsum);
            res = Math.max(res, Lmax + Msum);
        }
        Lsum = Lmax = Msum = Mmax = 0;
        for (int i = 0; i < A.length; ++i) {
            Lsum += A[i];
            if (i - L >= 0) Lsum -= A[i - L];
            if (i - L >= 0) Msum += A[i - L];
            if (i - M - L >= 0) Msum -= A[i - L - M];
            Mmax = Math.max(Mmax, Msum);
            res = Math.max(res, Mmax + Lsum);
        }
        return res;
    }
}
```

**C++:**
```
    int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
        for (int i = 1; i < A.size(); ++i)
            A[i] += A[i - 1];
        int res = A[L + M - 1], Lmax = A[L - 1], Mmax = A[M - 1];
        for (int i = L + M; i < A.size(); ++i) {
            Lmax = max(Lmax, A[i - M] - A[i - L - M]);
            Mmax = max(Mmax, A[i - L] - A[i - L - M]);
            res = max(res, max(Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L]));
        }
        return res;
    }
```

**Python:**
```
    def maxSumTwoNoOverlap(self, A, L, M):
        for i in xrange(1, len(A)):
            A[i] += A[i - 1]
        res, Lmax, Mmax = A[L + M - 1], A[L - 1], A[M - 1]
        for i in xrange(L + M, len(A)):
            Lmax = max(Lmax, A[i - M] - A[i - L - M])
            Mmax = max(Mmax, A[i - L] - A[i - L - M])
            res = max(res, Lmax + A[i] - A[i - M], Mmax + A[i] - A[i - L])
        return res
```

