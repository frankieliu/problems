
Python Easy Iterative and Recursive Solution

https://leetcode.com/problems/kth-smallest-element-in-a-bst/discuss/63829

* Lang:    python3
* Author:  girikuncoro
* Votes:   56

Recursive:

    def kthSmallest(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left)
        self.k -= 1
        if self.k == 0:
            self.res = node.val
            return
        self.helper(node.right)


Iterative:

    def kthSmallest(root, k):
        stack = []
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right
