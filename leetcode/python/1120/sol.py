In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1120.maximum-average-subtree.algorithms.json

[Python] Recursion

https://leetcode.com/problems/maximum-average-subtree/discuss/334120

* Lang:    python
* Author:  lee215
* Votes:   7

## **Complexity**
Time `O(N)`
Space `O(H)`

**Python:**
```python
    def maximumAverageSubtree(self, root):
        self.res = 0
        def helper(root):
            if not root: return [0, 0.0]
            n1, s1 = helper(root.left)
            n2, s2 = helper(root.right)
            n = n1 + n2 + 1
            s = s1 + s2 + root.val
            self.res = max(self.res, s / n)
            return [n, s]
        helper(root)
        return self.res
```

