#
# @lc app=leetcode id=117 lang=python
#
# [117] Populating Next Right Pointers in Each Node II
#
# https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/description/
#
# algorithms
# Medium (33.33%)
# Total Accepted:    166K
# Total Submissions: 497.9K
# Testcase Example:  '{}'
#
# Given a binary tree
#
#
# struct TreeLinkNode {
# ⁠ TreeLinkNode *left;
# ⁠ TreeLinkNode *right;
# ⁠ TreeLinkNode *next;
# }
#
#
# Populate each next pointer to point to its next right node. If there is no
# next right node, the next pointer should be set to NULL.
#
# Initially, all next pointers are set to NULL.
#
# Note:
#
#
# You may only use constant extra space.
# Recursive approach is fine, implicit stack space does not count as extra
# space for this problem.
#
#
# Example:
#
# Given the following binary tree,
#
#
# ⁠    1
# ⁠  /  \
# ⁠ 2    3
# ⁠/ \    \
# 4   5    7
#
#
# After calling your function, the tree should look like:
#
#
# ⁠    1 -> NULL
# ⁠  /  \
# ⁠ 2 -> 3 -> NULL
# ⁠/ \    \
# 4-> 5 -> 7 -> NULL
#
#
#
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root is None:
            return

        p0 = root
        conn, first = None, None

        # main parent level loop
        while p0:
            if conn:
                if p0.left:
                    conn.next = p0.left
                    conn = conn.next
                if p0.right:
                    conn.next = p0.right
                    conn = conn.next
            else:
                if p0.left:
                    conn = p0.left
                    first = conn
                if p0.right:
                    if conn:
                        conn.next = p0.right
                        conn = conn.next
                    else:
                        conn = p0.right
                        first = conn
            p0 = p0.next

        if first:
            self.connect(first)

test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, 2, 3, 4, None, None, 7])
    tmp = TreeNode(0)
    s = Solution()
    print(s.connect(tn))
    print(tn)
