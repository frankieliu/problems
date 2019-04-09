#
# @lc app=leetcode id=572 lang=python3
#
# [572] Subtree of Another Tree
#
# https://leetcode.com/problems/subtree-of-another-tree/description/
#
# algorithms
# Easy (41.07%)
# Total Accepted:    83K
# Total Submissions: 202.1K
# Testcase Example:  '[3,4,5,1,2]\n[4,1,2]'
#
#
# Given two non-empty binary trees s and t, check whether tree t has exactly
# the same structure and node values with a subtree of s. A subtree of s is a
# tree consists of a node in s and all of this node's descendants. The tree s
# could also be considered as a subtree of itself.
#
#
# Example 1:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return true, because t has the same structure and node values with a subtree
# of s.
#
#
# Example 2:
#
# Given tree s:
#
# ⁠    3
# ⁠   / \
# ⁠  4   5
# ⁠ / \
# ⁠1   2
# ⁠   /
# ⁠  0
#
# Given tree t:
#
# ⁠  4
# ⁠ / \
# ⁠1   2
#
# Return false.
#
#


class Solution:

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def toStr(r):
            if r is None:
                return "-"
            ll = toStr(r.left)
            rr = toStr(r.right)
            return "({},{},{})".format(r.val, ll, rr)
        sstr = toStr(s)
        tstr = toStr(t)
        return tstr in sstr


test = True
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([3, 4, 5, 1, 2])
    tn2 = arrayToTreeNode([4, 1, 2])
    tmp = TreeNode(0)
    s = Solution()
    print(s.isSubtree(tn, tn2))
