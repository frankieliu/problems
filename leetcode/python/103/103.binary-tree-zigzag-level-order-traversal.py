#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#
# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/
#
# algorithms
# Medium (40.05%)
# Total Accepted:    189.2K
# Total Submissions: 472.5K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the zigzag level order traversal of its nodes'
# values. (ie, from left to right, then right to left for the next level and
# alternate between).
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
# return its zigzag level order traversal as:
#
# [
# ⁠ [3],
# ⁠ [20,9],
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
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        dqr = deque()
        dql = deque()
        dqr.append([root, 0])
        out = []
        while dqr or dql:

            if dqr:
                out.append([])
            while dqr:
                el, lvl = dqr.popleft()
                if el.left:
                    dql.append([el.left, lvl+1])
                if el.right:
                    dql.append([el.right, lvl+1])
                print(lvl)
                out[lvl].append(el.val)

            if dql:
                out.append([])
            while dql:
                el, lvl = dql.pop()
                if el.right:
                    dqr.appendleft([el.right, lvl+1])
                if el.left:
                    dqr.appendleft([el.left, lvl+1])
                print(lvl)
                out[lvl].append(el.val)

        return out


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    # tn = arrayToTreeNode([3, 9, 20, None, None, 15, 7])
    tn = arrayToTreeNode([1, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    print(s.zigzagLevelOrder(tn))