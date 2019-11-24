In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1110.delete-nodes-and-return-forest.algorithms.json

[Java/Python] Recursion Solution

https://leetcode.com/problems/delete-nodes-and-return-forest/discuss/328853

* Lang:    python
* Author:  lee215
* Votes:   69

## **Intuition**
As I keep saying in my "courses",
solve tree problem with recursion first.
<br>

## **Explanation**
If a `node` is root (has no parent) and isn\'t deleted,
when will we add it to the `result`.
<br>

## **Complexity**
Time `O(N)`
Space `O(N)`

<br>

**Java:**
```java
    Set<Integer> to_delete_set;
    List<TreeNode> res = new ArrayList<>();
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        res = new ArrayList<>();
        to_delete_set = new HashSet<>();
        for (int i : to_delete)
            to_delete_set.add(i);
        helper(root, true);
        return res;
    }

    private TreeNode helper(TreeNode node, boolean is_root) {
        if (node == null) return null;
        boolean deleted = to_delete_set.contains(node.val);
        if (is_root && !deleted) res.add(node);
        node.left = helper(node.left, deleted);
        node.right =  helper(node.right, deleted);
        return deleted ? null : node;
    }
```

**Python:**
```python
    def delNodes(self, root, to_delete):
        to_delete_set = set(to_delete)
        res = []

        def helper(root, is_root):
            if not root: return None
            root_deleted = root.val in to_delete_set
            if is_root and not root_deleted:
                res.append(root)
            root.left = helper(root.left, root_deleted)
            root.right = helper(root.right, root_deleted)
            return None if root_deleted else root
        helper(root, True)
        return res
```

