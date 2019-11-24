In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1121.divide-array-into-increasing-sequences.algorithms.json

[Java/C++/Python] One Pass, O(1) Space and Prove

https://leetcode.com/problems/divide-array-into-increasing-sequences/discuss/334111

* Lang:    python
* Author:  lee215
* Votes:   31

## **Intuition**
For example 2: `A = [5,6,6,7,8]`
we have two 6, so we have to split `A` into at least two subsequence.
We want `K = 3` numbers in each subsequence, so we need at least  `K * 2 = 6` numbers.
But we have only `A.length = 5` numbers.
<br>

## **Explanation**
So the idea is that, find the maximum quantity of same numbers in `A`.
As `A` is sorted already, we can do this in one pass and `O(1)` space.
`cur` is the current length of same number until `A[i]`.
If `A[i - 1] < A[i]`, we reset `cur = 1`. Otherwise increment `cur = cur + 1`.

If `n < K * groups`, it\'s impossible to satisfy the condition, we return `false`.
Otherwise, we have enough numbers in hand and we can easily meet the requirement:
<br>

## Prove
Provide a way to split here:
1. Find the number of `groups` as in the solution, assume it equals to `M`
2. Assign `A[i]` to `groups[i % M]`.
3. Done.
<br>

## **Complexity**
Time `O(N)` for one pass, and you can return false earlier.
Space `O(1)` for no extra space.
<br>

**Java:**
```java
    public boolean canDivideIntoSubsequences(int[] A, int K) {
        int cur = 1, groups = 1, n = A.length;
        for (int i = 1; i < n; ++i) {
            cur = A[i - 1] < A[i] ?  1 : cur + 1;
            groups = Math.max(groups, cur);
        }
        return n >= K * groups;
    }
```

**C++:**
```cpp
    bool canDivideIntoSubsequences(vector<int>& A, int K) {
        int cur = 1, groups = 1, n = A.size();
        for (int i = 1; i < n; ++i) {
            cur = A[i - 1] <  A[i] ? 1 : cur + 1;
            groups = max(groups, cur);
        }
        return n >= K * groups;
    }
```

**Python, 1 line, O(N) space:**
```python
    def canDivideIntoSubsequences(self, A, K):
        return len(A) >= K * max(collections.Counter(A).values())
```

