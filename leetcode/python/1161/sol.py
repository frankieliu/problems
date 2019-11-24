In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1161.maximum-level-sum-of-a-binary-tree.algorithms.json

[Java/Python 3] Two codes / language: BFS level traversal and DFS level sum.

https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/discuss/360968

* Lang:    python
* Author:  rock
* Votes:   14

**Method 1: BFS**

Use BFS to find the sum of each level, then locate the level with largest sum.

**Java**

```
    public int maxLevelSum(TreeNode root) {
        int level = 1, max = Integer.MIN_VALUE, maxLevel = 1;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            int sum = 0; 
            for (int sz = q.size(); sz > 0; --sz) {
                TreeNode n = q.poll();
                sum += n.val;
                if (n.left != null) { q.offer(n.left); }
                if (n.right != null) { q.offer(n.right); }
            }
            if (max < sum) {
                max = sum;
                maxLevel = level;           
            }
            ++level;
        }
        return maxLevel;
    }
```

----

**Python 3**
```
    def maxLevelSum(self, root: TreeNode) -> int:
        max, level, maxLevel = -float(\'inf\'), 0, 0
        q = collections.deque()
        q.append(root)
        while q:
            level += 1
            sum = 0
            for _ in range(len(q)):
                node = q.popleft()
                sum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if max < sum:
                max, maxLevel = sum, level        
        return maxLevel
```

---------------------

**Method 2: DFS**
Use DFS to compute and store the sum of each level in an ArrayList, then locate the level with largest sum.
1. Recurse down from root, level of which is 0, increase level by 1 for each recursion down;
2. Use the level as the index of an ArrayList to store the sum of the correspoinding level;
3. Find the index of the max sum, then plus 1.

**Java**

```
    public int maxLevelSum(TreeNode root) {
        List<Integer> list = new ArrayList<>();
        dfs(root, list, 0);
        return 1 + IntStream.range(0, list.size()).reduce(0, (a, b) -> list.get(a) < list.get(b) ? b : a);
    }
    private void dfs(TreeNode n, List<Integer> l, int level) {
        if (n == null) { return; } 
        if (l.size() == level) { l.add(n.val); } // never reach this level before, add first value.
        else { l.set(level, l.get(level) + n.val); } // reached the level before, accumulate current value to old value.
        dfs(n.left, l, level + 1);
        dfs(n.right, l, level + 1);
    }
```
In case you are NOT comfortable with the Java 8 stream in the return statement, it can be written as:
```
        int maxLevel = 0;
        for (int i = 0; i < list.size(); ++i) {
            if (list.get(maxLevel) < list.get(i)) {
                maxLevel = i;
            }
        }
        return maxLevel + 1;
```

----

**Python 3**

```
    def maxLevelSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode, list: List, level: int) -> None:
            if not node:
                return
            if len(list) == level:
                list.append(node.val)
            else:
                list[level] += node.val
            dfs(node.left, list, level + 1)
            dfs(node.right, list, level + 1)
        list = []    
        dfs(root, list, 0)
        return 1 + list.index(max(list))
```

----

**Analysis:**

Time & space: O(n), n is the number of total nodes.
