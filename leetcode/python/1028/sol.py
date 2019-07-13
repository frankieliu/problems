In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1028.recover-a-tree-from-preorder-traversal.algorithms.json

[Java/C++/Python] Iterative Stack Solution

https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/discuss/274621

* Lang:    python
* Author:  lee215
* Votes:   55

## **Explanation**
We save the construction path in a `stack`.
In each loop,
we get the number `level` of `\'-\'`
we get the value `val` of `node` to add.

If the size of stack is bigger than the level of node,
we pop the stack until it\'s not.

Finally we return the first element in the stack, as it\'s root of our tree.

## **Complexity**

Time `O(S)`, Space `O(N)`


**Java**
```
    public TreeNode recoverFromPreorder(String S) {
        int level, val;
        Stack<TreeNode> stack = new Stack<>();
        for (int i = 0; i < S.length();) {
            for (level = 0; S.charAt(i) == \'-\'; i++) {
                level++;
            }
            for (val = 0; i < S.length() && S.charAt(i) != \'-\'; i++) {
                val = val * 10 + (S.charAt(i) - \'0\');
            }
            while (stack.size() > level) {
                stack.pop();
            }
            TreeNode node = new TreeNode(val);
            if (!stack.isEmpty()) {
                if (stack.peek().left == null) {
                    stack.peek().left = node;
                } else {
                    stack.peek().right = node;
                }
            }
            stack.add(node);
        }
        while (stack.size() > 1) {
            stack.pop();
        }
        return stack.pop();
    }
```

**C++**
```
    TreeNode* recoverFromPreorder(string S) {
        vector<TreeNode*> stack;
        for (int i = 0, level, val; i < S.length();) {
            for (level = 0; S[i] == \'-\'; i++)
                level++;
            for (val = 0; i < S.length() && S[i] != \'-\'; i++)
                val = val * 10 + S[i] - \'0\';
            TreeNode* node = new TreeNode(val);
            while (stack.size() > level) stack.pop_back();
            if (!stack.empty())
                if (!stack.back()->left) stack.back()->left = node;
                else stack.back()->right = node;
            stack.push_back(node);
        }
        return stack[0];
    }
```

**Python:**
```
    def recoverFromPreorder(self, S):
        stack, i = [], 0
        while i < len(S):
            level, val = 0, ""
            while i < len(S) and S[i] == \'-\':
                level, i = level + 1, i + 1
            while i < len(S) and S[i] != \'-\':
                val, i = val + S[i], i + 1
            while len(stack) > level:
                stack.pop()
            node = TreeNode(val)
            if stack and stack[-1].left is None:
                stack[-1].left = node
            elif stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
```


