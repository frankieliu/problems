#
# @lc app=leetcode id=285 lang=python3
#
# [285] Inorder Successor in BST
#
# https://leetcode.com/problems/inorder-successor-in-bst/description/
#
# algorithms
# Medium (33.71%)
# Total Accepted:    98.4K
# Total Submissions: 291.8K
# Testcase Example:  '[2,1,3]\n1'
#
# Given a binary search tree and a node in it, find the in-order successor of
# that node in the BST.
#
# The successor of a node p is the node with the smallest key greater than
# p.val.
#
#
#
# Example 1:
#
#
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the
# return value is of TreeNode type.
#
#
# Example 2:
#
#
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the
# answer is null.
#
#
#
#
# Note:
#
#
# If the given node has no in-order successor in the tree, return null.
# It's guaranteed that the values of the tree are unique.
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
    def inorderSuccessor(self, root, p):
        """
            Normal in order traversal

            When node is found:
            1. parent node ( look for the successor on your right )
            2. on a left branch ( you could be the successor )
            3. on the right branch ( the answer should be there already )
            return a tuple

            (status, node | None)
            status = False : not found
                     True  : found

            For case 1:
            - look for the leftmost child of the right node

            For case 2:
            - if the returned status is True, and the node is None
              then you must be the successor

            For case 3:
            - if the returned status is True, and the node is None, then
              there is no successor

        """

        def dfs(r, p):
            if r is None:
                return (False, None)
            # Case 1
            if r == p:
                if r.right is not None:
                    curr = r.right
                    while curr.left is not None:
                        curr = curr.left
                    return (True, curr)
                else:
                    return (True, None)

            # Case 2
            f, left = dfs(r.left, p)
            if f:
                if left is None:
                    return (f, r)
                else:
                    return (f, left)

            # Case 3
            f, right = dfs(r.right, p)
            if f:
                return (f, right)

            return (False, None)

        f, res = dfs(root, p)
        if f:
            return res
        else:
            return None


test = True
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([5, 3, 8, 2, 4, 6, 10])
    tmp = TreeNode(0)
    s = Solution()
    print(s.inorderSuccessor(tn, tn.right.right))
