#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
#
# https://leetcode.com/problems/binary-tree-right-side-view/description/
#
# algorithms
# Medium (46.17%)
# Total Accepted:    146.4K
# Total Submissions: 317.1K
# Testcase Example:  '[1,2,3,null,5,null,4]'
#
# Given a binary tree, imagine yourself standing on the right side of it,
# return the values of the nodes you can see ordered from top to bottom.
#
# Example:
#
#
# Input: [1,2,3,null,5,null,4]
# Output: [1, 3, 4]
# Explanation:
#
# ⁠  1            <---
# ⁠/   \
# 2     3         <---
# ⁠\     \
# ⁠ 5     4       <---
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
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        s = deque()
        s.append(root)

        n = deque()
        out = []

        while s:
            while s:
                el = s.popleft()
                if el.left:
                    n.append(el.left)
                if el.right:
                    n.append(el.right)
            # print(el.val, n)
            out.append(el.val)
            s = n
            n = deque()

        return out

test = True
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, 2, 3, 4, 5, 6])
    tn = arrayToTreeNode([1,2,3,None,5,None,4])
    tmp = TreeNode(0)
    s = Solution()
    print(s.rightSideView(tn))
