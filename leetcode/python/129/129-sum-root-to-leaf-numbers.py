#
# @lc app=leetcode id=129 lang=python3
#
# [129] Sum Root to Leaf Numbers
#
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
#
# algorithms
# Medium (41.00%)
# Total Accepted:    167.9K
# Total Submissions: 409.5K
# Testcase Example:  '[1,2,3]'
#
# Given a binary tree containing digits from 0-9 only, each root-to-leaf path
# could represent a number.
#
# An example is the root-to-leaf path 1->2->3 which represents the number 123.
#
# Find the total sum of all root-to-leaf numbers.
#
# Note: A leaf is a node with no children.
#
# Example:
#
#
# Input: [1,2,3]
# ⁠   1
# ⁠  / \
# ⁠ 2   3
# Output: 25
# Explanation:
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
#
# Example 2:
#
#
# Input: [4,9,0,5,1]
# ⁠   4
# ⁠  / \
# ⁠ 9   0
# / \
# 5   1
# Output: 1026
# Explanation:
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
#
#
# Definition for a binary tree node.

class Solution:

    def sumNumbers(self, root):
        def convert(a):
            sum = 0
            for i in range(0, len(a)):
                sum = a[i] + sum*10
            return sum

        def listNodes(root):
            if root.left is None or root.right is None:
                return [[root.val]]
            return ([[root.val]+x for x in listNodes(root.left)] +
                    [[root.val]+x for x in listNodes(root.right)])

        if root is None:
            return 0
        return sum(convert(x) for x in listNodes(root))


test = True
if test:
    class TreeNode:
        def __init__(self, x):
            self.val = x
            self.left = None
            self.right = None
    case = [False] * 3 + [True] + [False]*10
    if case[0]:
        tn = TreeNode(1)
        tn.left = TreeNode(2)
        tn.right = TreeNode(3)
        s = Solution()
        print(s.sumNumbers(tn))

    if case[1]:
        # Input: [4,9,0,5,1]
        # ⁠    4
        # ⁠   / \
        #  ⁠ 9   0
        #  / \
        # 5   1
        tn = TreeNode(4)
        tn.left = TreeNode(9)
        tn.right = TreeNode(0)
        tn.left.left = TreeNode(5)
        tn.left.right = TreeNode(1)
        s = Solution()
        print(s.sumNumbers(tn))
    if case[2]:
        # Input: [4,9,0,5,1]
        # ⁠    4
        # ⁠   / \
        #  ⁠ 9   0
        #  / \
        # 5   1
        tn = TreeNode(1)
        print(s.sumNumbers(tn))
    if case[3]:
        # Input: [4,9,0,5,1]
        # ⁠    4
        # ⁠   / \
        #  ⁠ 9   0
        #  / \
        # 5   1
        tn = None
        print(s.sumNumbers(tn))
