
1 line Ruby and Python

https://leetcode.com/problems/maximum-depth-of-binary-tree/discuss/34212

* Lang:    python3
* Author:  StefanPochmann
* Votes:   51

Just a bit shorter/different than previous solutions.

Ruby:

    def max_depth(root)
      root ? 1 + [max_depth(root.left), max_depth(root.right)].max : 0
    end

Python:

    def maxDepth(self, root):
        return 1 + max(map(self.maxDepth, (root.left, root.right))) if root else 0
