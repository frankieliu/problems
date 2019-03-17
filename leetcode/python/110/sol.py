
VERY SIMPLE Python solutions (iterative and recursive), both beat 90%

https://leetcode.com/problems/balanced-binary-tree/discuss/35708

* Lang:    python3
* Author:  agave
* Votes:   67

```  
class Solution(object):
    def isBalanced(self, root):
            
        def check(root):
            if root is None:
                return 0
            left  = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
            
        return check(root) != -1

# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 80 ms
```


Iterative, based on postorder traversal:

```
class Solution(object):
    def isBalanced(self, root):
        stack, node, last, depths = [], root, None, {}
        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if not node.right or last == node.right:
                    node = stack.pop()
                    left, right  = depths.get(node.left, 0), depths.get(node.right, 0)
                    if abs(left - right) > 1: return False
                    depths[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True


# 226 / 226 test cases passed.
# Status: Accepted
# Runtime: 84 ms

```
