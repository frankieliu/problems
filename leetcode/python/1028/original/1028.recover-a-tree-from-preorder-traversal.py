#
# @lc app=leetcode id=1028 lang=python
#
# [1028] Recover a Tree From Preorder Traversal
#
# https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/description/
#
# algorithms
# Hard (70.05%)
# Total Accepted:    6.8K
# Total Submissions: 9.8K
# Testcase Example:  '"1-2--3--4-5--6--7"'
#
# We run a preorder depth first search on the root of a binary tree.
# 
# At each node in this traversal, we output D dashes (where D is the depth of
# this node), then we output the value of this node.  (If the depth of a node
# is D, the depth of its immediate child is D+1.  The depth of the root node is
# 0.)
# 
# If a node has only one child, that child is guaranteed to be the left child.
# 
# Given the output S of this traversal, recover the tree and return its
# root.
# 
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: "1-2--3--4-5--6--7"
# Output: [1,2,5,3,4,6,7]
# 
# 
# 
# Example 2:
# 
# 
# 
# 
# Input: "1-2--3---4-5--6---7"
# Output: [1,2,5,3,null,6,null,4,null,7]
# 
# 
# 
# 
# 
# 
# Example 3:
# 
# 
# 
# 
# Input: "1-401--349---90--88"
# Output: [1,401,null,349,88,90]
# 
# 
# 
# 
# 
# Note:
# 
# 
# The number of nodes in the original tree is between 1 and 1000.
# Each node will have a value between 1 and 10^9.
# 
# 
# 
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverFromPreorder(self, S):
        """
        :type S: str
        :rtype: TreeNode
        """
        
