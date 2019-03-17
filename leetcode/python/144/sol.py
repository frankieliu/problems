
Very simple iterative Python solution

https://leetcode.com/problems/binary-tree-preorder-traversal/discuss/45273

* Lang:    python3
* Author:  clue
* Votes:   56

Classical usage of stack's LIFO feature, very easy to grasp:

    
    def preorderTraversal(self, root):
        ret = []
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                ret.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return ret
