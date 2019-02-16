#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
#
# algorithms
# Medium (37.51%)
# Total Accepted:    137.3K
# Total Submissions: 366K
# Testcase Example:  '[9,3,15,20,7]\n[9,15,7,20,3]'
#
# Given inorder and postorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# inorder = [9,3,15,20,7]
# postorder = [9,15,7,20,3]
#
# Return the following binary tree:
#
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
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
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        if len(inorder) == 0:
            return None
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        # inorder left root right
        # postorder left right root
        n = len(postorder)
        root = postorder[n-1]
        root_idx = inorder.index(root)
        left_tree = self.buildTree(
            inorder[0:root_idx], postorder[0:root_idx])
        right_tree = self.buildTree(
            inorder[root_idx+1:], postorder[root_idx:-1])
        tn = TreeNode(root)
        tn.left = left_tree
        tn.right = right_tree
        return tn


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, None, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    inorder = [9, 3, 15, 20, 7]
    postorder = [9, 15, 7, 20, 3]
    print(s.buildTree(inorder, postorder))
