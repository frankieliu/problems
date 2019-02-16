#
# @lc app=leetcode id=114 lang=python3
#
# [114] Flatten Binary Tree to Linked List
#
# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
#
# algorithms
# Medium (40.65%)
# Total Accepted:    214.2K
# Total Submissions: 527K
# Testcase Example:  '[1,2,5,3,4,null,6]'
#
# Given a binary tree, flatten it to a linked list in-place.
#
# For example, given the following tree:
#
#
# ⁠   1
# ⁠  / \
# ⁠ 2   5
# ⁠/ \   \
# 3   4   6
#
#
# The flattened tree should look like:
#
#
# 1
# ⁠\
# ⁠ 2
# ⁠  \
# ⁠   3
# ⁠    \
# ⁠     4
# ⁠      \
# ⁠       5
# ⁠        \
# ⁠         6
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
    def flatten(self, root):
        if root is None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        if root.left:
            # find right most
            tmp = root.left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root.right
            root.right = root.left
            root.left = None

    # This is for "real" binary tree
    def flatten_help(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if root is None:
            return root
        if root.left is None and root.right is None:
            return root

        if root.left:
            left = self.flatten(root.left)
        else:
            left = None

        if root.right:
            right = self.flatten(root.right)
        else:
            right = None

        if left:
            # find rightmost
            tmp = left
            while tmp.right:
                tmp = tmp.right
            tmp.right = root
            root.right = right
            root.left = None
            return left
        else:
            root.right = right
            return root


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, 2, 5, 3, 4, None, 6])
    tmp = TreeNode(0)
    s = Solution()
    print(s.flatten(tn))
    print(tn)
