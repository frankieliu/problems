
My Python recursive solution

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/discuss/65183

* Lang:    python3
* Author:  Bluryi
* Votes:   13



    class Solution:
        # @param {TreeNode} root
        # @param {TreeNode} p
        # @param {TreeNode} q
        # @return {TreeNode}
        def lowestCommonAncestor(self, root, p, q):
            if not root or not p or not q:
                return None
            if (max(p.val, q.val) < root.val):
                return self.lowestCommonAncestor(root.left, p, q)
            elif (min(p.val, q.val) > root.val):
                return self.lowestCommonAncestor(root.right, p, q)
            else:
                return root
