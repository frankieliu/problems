#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/
#
# algorithms
# Medium (54.46%)
# Total Accepted:    394.9K
# Total Submissions: 725.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the inorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [1,3,2]
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        out = []
        lo = self.inorderTraversal(root.left)
        ro = self.inorderTraversal(root.right)
        out.extend(lo)
        out.append(root.val)
        out.extend(ro)
        return out


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1,None,2,3])
    s = Solution()
    print(s.inorderTraversal(tn))
    tn = arrayToTreeNode([])
    s = Solution()
    print(s.inorderTraversal(tn))
