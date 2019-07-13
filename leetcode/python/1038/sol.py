In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1038.binary-search-tree-to-greater-sum-tree.algorithms.json

[Java/C++/Python] Revered Inorder Traversal

https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/discuss/286725

* Lang:    python
* Author:  lee215
* Votes:   32

We need to do the work from biggest to smallest, right to left.
`pre` will record the previous value the we get, which the total sum of bigger values.
For each node, we update `root.val` with `root.val + pre`.

<br>

**Java:**
```
    int pre = 0;
    public TreeNode bstToGst(TreeNode root) {
        if (root.right != null) bstToGst(root.right);
        pre = root.val = pre + root.val;
        if (root.left != null) bstToGst(root.left);
        return root;
    }
```

**C++:**
```
    int pre = 0;
    TreeNode* bstToGst(TreeNode* root) {
        if (root->right) bstToGst(root->right);
        pre = root->val = pre + root->val;
        if (root->left) bstToGst(root->left);
        return root;
    }
```

**Python:**
```
    val = 0
    def bstToGst(self, root):
        if root.right: self.bstToGst(root.right)
        root.val = self.val = self.val + root.val
        if root.left: self.bstToGst(root.left)
        return root
```

