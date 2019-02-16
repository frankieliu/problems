#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-level-order-traversal/description/
#
# algorithms
# Medium (46.51%)
# Total Accepted:    324.2K
# Total Submissions: 697K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the level order traversal of its nodes' values.
# (ie, from left to right, level by level).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [9,20],
# ⁠ [15,7]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        dq = deque()
        dq.append([root, 0])
        out = []
        while dq:
            el, lvl = dq.popleft()
            if el.left:
                dq.append([el.left, lvl+1])
            if el.right:
                dq.append([el.right, lvl+1])
            if lvl > len(out)-1:
                out.append([])
            out[lvl].append(el.val)
        return out


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([])
    tmp = TreeNode(0)
    s = Solution()
    print(s.levelOrder(tn))
