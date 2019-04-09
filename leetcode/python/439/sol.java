
O(1) space O(n) time java solution; using an int to simulate stack and pre-order traversal

https://leetcode.com/problems/ternary-expression-parser/discuss/92193

* Lang:    java
* Author:  ollie
* Votes:   0

It is similar with pre-order traversal of the binary tree. 
1. We scan from left to right. For each condition checking, if it is T, then we will dive into the left sub-tree; otherwise, into right sub-tree;
2. *stack* variable indicates number of sub-tree to traverse to approach the sub-tree that the answer resides. For example, in tree F?1:2, *stack*=2; while in F?T?1:2:3, *stack*=3 at root.
3. When *stack* becomes 0, we find the answer; otherwise, continue on traversal.
```
public String parseTernary(String expression) {
        if (expression == null || expression.length() == 0) return "";
        
        int n = expression.length();
        int stack = 0;
        if (expression.charAt(0) == 'T') stack = 1;
        else stack = 2;
        int idx = 2;
        while (stack > 0) {
            stack--;
            if (idx + 1 < n && expression.charAt(idx + 1) == '?') {
                if (stack == 0 && expression.charAt(idx) == 'T') stack = 1;
                else stack += 2;
            }
            idx += 2;
        }
        return "" + expression.charAt(idx - 2);
    }
```
