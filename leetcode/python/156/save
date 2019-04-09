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

# ⁠   1
# ⁠  / \
# ⁠ 2   3
# ⁠/ \
# 4   5


class Solution:
    def upsideDownBinaryTree(self, r):
        def _up(root):
            if root is None:
                return root, None
            if root.left is None:  # leaf node
                return root, root
            new_root, new_right = _up(root.left)
            print(new_root, new_right)
            new_right.left = root.right
            new_right.right = root
            root.left = None
            root.right = None
            return new_root, root

        nr, _ = _up(r)
        return nr



test = True
if test:
    Input = [1, 2, 3, 4, 5]
    Input = [1, 2, None, 3, None, 4]
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode(Input)
    tmp = TreeNode(0)
    s = Solution()
    #
    # ⁠    1
    # ⁠   / \
    #  ⁠ 2   3
    #  ⁠/ \
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
    #  Think of a 90 degree clockwise rotation
    print(s.upsideDownBinaryTree(tn))
