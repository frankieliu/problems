#
# @lc app=leetcode id=156 lang=python3
#
# [156] Binary Tree Upside Down
#
# https://leetcode.com/problems/binary-tree-upside-down/description/
#
# algorithms
# Medium (49.73%)
# Total Accepted:    44.6K
# Total Submissions: 89.7K
# Testcase Example:  '[1,2,3,4,5]'
#
# Given a binary tree where all the right nodes are either leaf nodes with a
# sibling (a left node that shares the same parent node) or empty, flip it
# upside down and turn it into a tree where the original right nodes turned
# into left leaf nodes. Return the new root.
# 
# Example:
# 
# 
# Input: [1,2,3,4,5]
# 
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \
# 4   5
# 
# Output: return the root of the binary tree [4,5,2,#,#,3,1]
# 
# ⁠  4
# ⁠ / \
# ⁠5   2
# ⁠   / \
# ⁠  3   1  
# 
# 
# Clarification:
# 
# Confused what [4,5,2,#,#,3,1] means? Read more below on how binary tree is
# serialized on OJ.
# 
# The serialization of a binary tree follows a level order traversal, where '#'
# signifies a path terminator where no node exists below.
# 
# Here's an example:
# 
# 
# ⁠  1
# ⁠ / \
# ⁠2   3
# ⁠   /
# ⁠  4
# ⁠   \
# ⁠    5
# 
# 
# The above binary tree is serialized as [1,2,3,#,#,4,#,#,5].
# 
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        
