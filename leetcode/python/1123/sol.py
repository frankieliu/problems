In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1123.lowest-common-ancestor-of-deepest-leaves.algorithms.json

[Java/C++/Python] Two Recursive Solution

https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/discuss/334577

* Lang:    python
* Author:  lee215
* Votes:   42

# **Complexity**
Both solution are one pass.
Time `O(N)` for one pass
Space `O(H)` for recursion management
<br>

# Solution 1: Get Subtree Height and LCA
`helper` function return the subtree `height` and `lca` and  at the same time.
`null` node will return depth 0,
leaves will return depth 1.


<br>

**C++**
```cpp
    pair<TreeNode*, int> helper(TreeNode* root) {
        if (!root) return {NULL, 0};
        auto left = helper(root->left);
        auto right = helper(root->right);
        if (left.second > right.second)
            return {left.first, left.second + 1};
        if (left.second < right.second)
            return {right.first, right.second + 1};
        return {root, left.second + 1};

    }
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        return helper(root).first;
    }
```

**Python:**
```python
    def lcaDeepestLeaves(self, root):
        def helper(root):
            if not root: return 0, None
            h1, lca1 = helper(root.left)
            h2, lca2 = helper(root.right)
            if h1 > h2: return h1 + 1, lca1
            if h1 < h2: return h2 + 1, lca2
            return h1 + 1, root
        return helper(root)[1]
```

**Java**
from @timmy2
```java
    class Pair {
        TreeNode node;
        int d;
        Pair(TreeNode node, int d) {
            this.node = node;
            this.d = d;
        }
    }
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        Pair p = getLca(root, 0);
        return p.node;
    }
    private Pair getLca(TreeNode root, int d) {
        if (root == null) return new Pair(null, d);
        Pair l = getLca(root.left, d + 1);
        Pair r = getLca(root.right, d + 1);
        if (l.d == r.d) {
            return new Pair(root, l.d);
        } else {
            return  l.d > r.d ? l : r;
        }
    }
```
<br>

# Solution 2: Get Subtree Deepest Depth
`helper` function return the deepest depth of descendants.
`deepest` represent the deepest depth.
We use a global variable `lca` to represent the result.
One pass, Time `O(N)` Space `O(H)`
<br>

**Java:**
inspired by @Brahms
```java
    int deepest = 0;
    TreeNode lca;

    public TreeNode lcaDeepestLeaves(TreeNode root) {
        helper(root, 0);
        return lca;
    }

    private int helper(TreeNode node, int depth) {
        deepest = Math.max(deepest, depth);
        if (node == null) {
            return depth;
        }
        int left = helper(node.left, depth + 1);
        int right = helper(node.right, depth + 1);
        if (left == deepest && right == deepest) {
            lca = node;
        }
        return Math.max(left, right);
    }
```

**C++:**
```cpp
    TreeNode* lca;
    int deepest = 0;
    TreeNode* lcaDeepestLeaves(TreeNode* root) {
        helper(root, 0);
        return lca;
    }

    int helper(TreeNode* node, int depth) {
        deepest = max(deepest, depth);
        if (!node) {
            return depth;
        }
        int left = helper(node->left, depth + 1);
        int right = helper(node->right, depth + 1);
        if (left == deepest && right == deepest) {
            lca = node;
        }
        return max(left, right);
    }
```

**Python:**
```python
    def lcaDeepestLeaves(self, root):
        self.lca, self.deepest = None, 0
        def helper(node, depth):
            self.deepest = max(self.deepest, depth)
            if not node:
                return depth
            left = helper(node.left, depth + 1)
            right = helper(node.right, depth + 1)
            if left == right == self.deepest:
                self.lca = node
            return max(left, right)
        helper(root, 0)
        return self.lca
```

