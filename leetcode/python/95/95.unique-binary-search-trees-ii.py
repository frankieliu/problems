#
# @lc app=leetcode id=95 lang=python3
#
# [95] Unique Binary Search Trees II
#
# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
#
# algorithms
# Medium (34.49%)
# Total Accepted:    125.3K
# Total Submissions: 363.4K
# Testcase Example:  '3'
#
# Given an integer n, generate all structurally unique BST's (binary search
# trees) that store values 1 ... n.
#
# Example:
#
#
# Input: 3
# Output:
# [
# [1,null,3,2],
# [3,2,null,1],
# [3,1,null,null,2],
# [2,1,3],
# [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
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
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        return self.helper(list(range(1, n+1)))

    def helper(self, a):

        if len(a) == 1:
            return [TreeNode(a[0])]

        out = []
        for i in range(0, len(a)):
            if i == 0:
                lt = [None]
            else:
                lt = self.helper(a[0:i])

            if i == len(a)-1:
                rt = [None]
            else:
                rt = self.helper(a[i+1:])

            for ll in lt:
                for rr in rt:
                    root = TreeNode(a[i])
                    root.left = ll
                    root.right = rr
                    out.append(root)
        return out


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, None, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    print(s.generateTrees(3))
