In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1026.maximum-difference-between-node-and-ancestor.algorithms.json

[Java/C++/Python] Top Down

https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/discuss/274610

* Lang:    python
* Author:  lee215
* Votes:   69

We pass the minimum and maximum values to the children,
At the leaf node, we return `max - min` through the path from the root to the leaf.


**Java:**
```
    public int maxAncestorDiff(TreeNode root) {
        return dfs(root, root.val, root.val);
    }

    public int dfs(TreeNode root, int mn, int mx) {
        if (root == null) return mx - mn;
        mx = Math.max(mx, root.val);
        mn = Math.min(mn, root.val);
        return Math.max(dfs(root.left, mn, mx), dfs(root.right, mn, mx));
    }
```

**C++ 1-line**
```
    int maxAncestorDiff(TreeNode* r, int mn = 100000, int mx = 0) {
        return r ? max(maxAncestorDiff(r->left, min(mn, r->val), max(mx, r->val)),
        maxAncestorDiff(r->right, min(mn, r->val), max(mx, r->val))) : mx - mn;
    }
```
**Python 1-line**
```
    def maxAncestorDiff(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)), \\
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \\
            if root else mx - mn
```

