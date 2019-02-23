#
# @lc app=leetcode id=109 lang=python3
#
# [109] Convert Sorted List to Binary Search Tree
#
# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/description/
#
# algorithms
# Medium (39.13%)
# Total Accepted:    160.7K
# Total Submissions: 410.7K
# Testcase Example:  '[-10,-3,0,5,9]'
#
# Given a singly linked list where elements are sorted in ascending order,
# convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more
# than 1.
#
# Example:
#
#
# Given the sorted linked list: [-10,-3,0,5,9],
#
# One possible answer is: [0,-3,9,-10,null,5], which represents the following
# height balanced BST:
#
# ⁠     0
# ⁠    / \
# ⁠  -3   9
# ⁠  /   /
# ⁠-10  5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        a = []
        while head:
            a.append(head.val)
            head = head.next
        return self.arrayToBST(a)

    def arrayToBST(self, a):
        if len(a) == 0:
            return None
        if len(a) == 1:
            return TreeNode(a[0])

        mid = len(a) // 2
        tn = TreeNode(a[mid])
        left = self.arrayToBST(a[0:mid])
        right = self.arrayToBST(a[mid+1:])
        tn.left = left
        tn.right = right
        return tn

test = False
if test:
    from ListNode.ListNode import ListNode
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode

    ll = ListNode.make([1, 2, 3, 4, 5, 6])
    s = Solution()
    print(s.sortedListToBST(ll))