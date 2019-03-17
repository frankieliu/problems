
8-10 lines, two solutions

https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/39919

* Lang:    python3
* Author:  StefanPochmann
* Votes:   22

Two solutions:

---

**Solution 1: *Helper returning two values*:** (240 ms, 8 lines)

    def maxPathSum(self, root):
        def maxsums(node):
            if not node:
                return [-2**31] * 2
            left = maxsums(node.left)
            right = maxsums(node.right)
            return [node.val + max(left[0], right[0], 0),
                    max(left + right + [node.val + left[0] + right[0]])]
        return max(maxsums(root))

My helper function returns two values:

 1. The max sum of all paths ending in the given node (can be extended through the parent)
 2. The max sum of all paths anywhere in tree rooted at the given node (can *not* be extended through the parent).


---

**Solution 2: *Helper updating a "global" maximum*:** (172 ms, 10 lines)

    def maxPathSum(self, root):
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0)
        self.max = None
        maxend(root)
        return self.max

Here the helper is similar, but only returns the first of the two values (the max sum of all paths ending in the given node). Instead of returning the second value (the max sum of all paths anywhere in tree rooted at the given node), it updates a "global" maximum.
