In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1144.decrease-elements-to-make-array-zigzag.algorithms.json

[Java/C++/Python] Easy and concise

https://leetcode.com/problems/decrease-elements-to-make-array-zigzag/discuss/350576

* Lang:    python
* Author:  lee215
* Votes:   56

## **Explanation**
Two options, either make `A[even]` smaller or make `A[odd]` smaller.
Loop on the whole array `A`,
find the `min(A[i - 1],A[i + 1])`,
calculate that the moves need to make smaller than both side.
If it\'s negative, it means it\'s already smaller than both side, no moved needed.
Add the moves need to `res[i%i]`.
In the end return the smaller option.
<br>

## **Complexity**
Time `O(N)` for one pass
Space `O(2)` for two options
<br>

**Java:**
```java
    public int movesToMakeZigzag(int[] A) {
        int res[] = new int[2],  n = A.length, left, right;
        for (int i = 0; i < n; ++i) {
            left = i > 0 ? A[i - 1] : 1001;
            right = i + 1 < n ? A[i + 1] : 1001;
            res[i % 2] += Math.max(0, A[i] - Math.min(left, right) + 1);
        }
        return Math.min(res[0], res[1]);
    }
```

**C++:**
```cpp
    int movesToMakeZigzag(vector<int>& A) {
        int res[2] = {0, 0},  n = A.size(), left, right;
        for (int i = 0; i < n; ++i) {
            left = i > 0 ? A[i - 1] : 1001;
            right = i + 1 < n ? A[i + 1] : 1001;
            res[i % 2] += max(0, A[i] - min(left, right) + 1);
        }
        return min(res[0], res[1]);
    }
```

**Python:**
```python
    def movesToMakeZigzag(self, A):
        A = [float(\'inf\')] + A + [float(\'inf\')]
        res = [0, 0]
        for i in xrange(1, len(A) - 1):
            res[i % 2] += max(0, A[i] - min(A[i - 1], A[i + 1]) + 1)
        return min(res)
```

