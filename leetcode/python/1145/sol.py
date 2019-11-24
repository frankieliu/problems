In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1145.binary-tree-coloring-game.algorithms.json

[Java/C++/Python] Simple recursion and Follow-Up

https://leetcode.com/problems/binary-tree-coloring-game/discuss/350570

* Lang:    python
* Author:  lee215
* Votes:   56

## **Intuition**
The first player colors a node,
there are at most 3 nodes connected to this node.
Its left, its right and its parent.
Take this 3 nodes as the root of 3 subtrees.

The second player just color any one root,
and the whole subtree will be his.
And this is also all he can take,
since he cannot cross the node of the first player.
<br>

## **Explanation**
`count` will recursively count the number of nodes,
in the left and in the right.
`n - left - right` will be the number of nodes in the "subtree" of parent.
Now we just need to compare `max(left, right, parent)` and `n / 2`
<br>

## **Complexity**
Time `O(N)`
Space `O(height)` for recursion
<br>

**Java:**
```java
    int left, right, val;
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        val = x;
        count(root);
        return Math.max(Math.max(left, right), n - left - right - 1) > n / 2;
    }

    private int count(TreeNode node) {
        if (node == null) return 0;
        int l = count(node.left), r = count(node.right);
        if (node.val == val) {
            left = l;
            right = r;
        }
        return l + r + 1;
    }
```

**C++:**
```cpp
    int left, right, val;
    bool btreeGameWinningMove(TreeNode* root, int n, int x) {
        val = x, n = count(root);
        return max(max(left, right), n - left - right - 1) > n / 2;
    }

    int count(TreeNode* node) {
        if (!node) return 0;
        int l = count(node->left), r = count(node->right);
        if (node->val == val)
            left = l, right = r;
        return l + r + 1;
    }
```

**Python:**
```python
    def btreeGameWinningMove(self, root, n, x):
        c = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                c[0], c[1] = l, r
            return l + r + 1
        return count(root) / 2 < max(max(c), n - sum(c) - 1)
```

## **Fun Moment of Follow-up**:
Alex and Lee are going to play this turned based game.
Alex draw the whole tree. `root` and `n` will be given.
Now Lee says he want to color the first node.
1. Return `true` if Lee can ensure his win, otherwise return `false`
2. Could you find the set all the nodes, that Lee can ensure he wins the game?
3. What is the complexity of your solution?
