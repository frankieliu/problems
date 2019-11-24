In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1130.minimum-cost-tree-from-leaf-values.algorithms.json

One Pass, O(N) Time and Space

https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959

* Lang:    python
* Author:  lee215
* Votes:   282

# Solution DP
Find the cost for the interval `[i,j]`.
To build up the interval `[i,j]`,
we need to split it into left subtree and sub tree,
`dp[i, j] = dp[i, k] + dp[k + 1, j] + max(A[i, k]) * max(A[k + 1, j])`

This solution is `O(N^3)` time and `O(N^2)` space. You think it\'s fine.
After several nested for loop, you get a green accepted and release a sigh.

Great practice for DP!
Then you think that\'s it for a medium problem, nothing can stop you.

so you didn\'t **read** and **up-vote** my post.
One day, you bring this solution to an interview and probably fail.
<br>

# **Intuition**
When we build a node in the tree, we compared the two numbers `a` and `b`.
In this process,
the smaller one is removed and we won\'t use it anymore,
and the bigger one actually stays.

The problem can translated as following:
Given an array `A`, choose two neighbors in the array `a` and `b`,
we can remove the smaller one `min(a,b)` and the cost is `a * b`.
What is the minimum cost to remove the whole array until only one left?

To remove a number `a`, it needs a cost `a * b`, where `b >= a`.
So `a` has to be removed by a bigger number.
We want minimize this cost, so we need to minimize `b`.

`b` has two candidates, the first bigger number on the left,
the first bigger number on the right.

The cost to remove `a` is `a * min(left, right)`.
<br>

# **Explanation**
Now we know that, this is not a dp problem.
(Because dp solution test all ways to build up the tree, it\'s kinda of brute force)

With the intuition above in mind,
we decompose a hard problem into reasonable easy one:
Just find the next greater element in the array, on the left and one right.
Refer to [1019. Next Greater Node In Linked List](https://leetcode.com/problems/next-greater-node-in-linked-list/discuss/265508/JavaC++Python-Next-Greater-Element)
<br>

# **Complexity**
Time `O(N)` for one pass
Space `O(N)` for stack in the worst cases
<br>

**Java:**
```java
    public int mctFromLeafValues(int[] A) {
        int res = 0, n = A.length;
        Stack<Integer> stack = new Stack<>();
        stack.push(Integer.MAX_VALUE);
        for (int a : A) {
            while (stack.peek() <= a) {
                int mid = stack.pop();
                res += mid * Math.min(stack.peek(), a);
            }
            stack.push(a);
        }
        while (stack.size() > 2) {
            res += stack.pop() * stack.peek();
        }
        return res;
    }
```

**C++:**
```cpp
    int mctFromLeafValues(vector<int>& A) {
        int res = 0, n = A.size();
        vector<int> stack = {INT_MAX};
        for (int a : A) {
            while (stack.back() <= a) {
                int mid = stack.back();
                stack.pop_back();
                res += mid * min(stack.back(), a);
            }
            stack.push_back(a);
        }
        for (int i = 2; i < stack.size(); ++i) {
            res += stack[i] * stack[i - 1];
        }
        return res;
    }
```

**Python:**
```python
    def mctFromLeafValues(self, A):
        res, n = 0, len(A)
        stack = [float(\'inf\')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack)  >2:
            res += stack.pop() * stack[-1]
        return res
```

