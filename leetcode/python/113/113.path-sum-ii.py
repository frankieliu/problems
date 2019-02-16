#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# https://leetcode.com/problems/path-sum-ii/description/
#
# algorithms
# Medium (39.04%)
# Total Accepted:    208.2K
# Total Submissions: 533.4K
# Testcase Example:  '[5,4,8,11,null,13,4,7,2,null,null,5,1]\n22'
#
# Given a binary tree and a sum, find all root-to-leaf paths where each path's
# sum equals the given sum.
#
# Note: A leaf is a node with no children.
#
# Example:
#
# Given the below binary tree and sum = 22,
#
#
# ⁠     5
# ⁠    / \
# ⁠   4   8
# ⁠  /   / \
# ⁠ 11  13  4
# ⁠/  \    / \
# 7    2  5   1
#
#
# Return:
#
#
# [
# ⁠  [5,4,11,2],
# ⁠  [5,8,4,5]
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

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root is None:
            return []
        out = []
        path = []
        self.helper(root, sum, path, out)
        return out

    def helper(self, root, sum, path, out):
        if root is None:
            if sum == 0:
                out.append(path[:])
            return
        path.append(root.val)

        if root.left is None and root.right is None:
            if sum - root.val == 0:
                out.append(path[:])
        else:
            if root.left is not None:
                self.helper(root.left, sum - root.val, path, out)
            if root.right is not None:
                self.helper(root.right, sum - root.val, path, out)
        path.pop()
        return


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
    tmp = TreeNode(0)
    s = Solution()
    print(s.pathSum(tn, 22))
