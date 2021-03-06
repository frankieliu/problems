#
# @lc app=leetcode id=543 lang=python3
#
# [543] Diameter of Binary Tree
#
# https://leetcode.com/problems/diameter-of-binary-tree/description/
#
# algorithms
# Easy (46.07%)
# Total Accepted:    106.9K
# Total Submissions: 232.1K
# Testcase Example:  '[1,2,3,4,5]'
#
#
# Given a binary tree, you need to compute the length of the diameter of the
# tree. The diameter of a binary tree is the length of the longest path between
# any two nodes in a tree. This path may or may not pass through the root.
#
#
#
# Example:
# Given a binary tree
#
# ⁠         1
# ⁠        / \
# ⁠       2   3
# ⁠      / \
# ⁠     4   5
#
#
#
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#
#
# Note:
# The length of path between two nodes is represented by the number of edges
# between them.
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def longLeaf(r):
            if r is None:
                return 0, 0
            ll, lp = longLeaf(r.left)
            rl, rp = longLeaf(r.right)
            offl, offr = 0, 0
            if r.left is None:
                offl = -1
            if r.right is None:
                offr = -1
            cp = max([lp, rp, ll+rl+2+offl+offr])
            cl = max([ll+offl, rl+offr]) + 1
            print(r, cp, cl)
            return cl, cp
        nl, np = longLeaf(root)
        return np


test = True
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, 2, 3, 4])
    tmp = TreeNode(0)
    s = Solution()
    print(s.diameterOfBinaryTree(tn))
