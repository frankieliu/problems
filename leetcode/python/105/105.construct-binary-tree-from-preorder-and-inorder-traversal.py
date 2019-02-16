#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#
# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/
#
# algorithms
# Medium (38.91%)
# Total Accepted:    193.9K
# Total Submissions: 498.3K
# Testcase Example:  '[3,9,20,15,7]\n[9,3,15,20,7]'
#
# Given preorder and inorder traversal of a tree, construct the binary tree.
#
# Note:
# You may assume that duplicates do not exist in the tree.
#
# For example, given
#
#
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
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
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # preorder root left right
        # inorder left root right

        if len(preorder) == 0:
            return None

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        # find the root in the inorder
        in_root_idx = inorder.index(preorder[0])

        left_tree = self.buildTree(
            preorder[1:in_root_idx+1], inorder[0:in_root_idx])
        right_tree = self.buildTree(
            preorder[in_root_idx+1:], inorder[in_root_idx+1:])

        tn = TreeNode(preorder[0])
        tn.left = left_tree
        tn.right = right_tree

        return tn

test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, None, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    print(s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7]))
