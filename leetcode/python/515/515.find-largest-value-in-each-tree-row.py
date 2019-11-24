#
# @lc app=leetcode id=515 lang=python3
#
# [515] Find Largest Value in Each Tree Row
#
# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
#
# algorithms
# Medium (57.04%)
# Total Accepted:    56.7K
# Total Submissions: 99.4K
# Testcase Example:  '[1,3,2,5,3,null,9]'
#
# You need to find the largest value in each row of a binary tree.
#
# Example:
#
# Input:
#
# ⁠         1
# ⁠        / \
# ⁠       3   2
# ⁠      / \   \
# ⁠     5   3   9
#
# Output: [1, 3, 9]
#
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def largestValues(self, root):
        q = deque()
        res = []
        while q:
            res.append(max(q))
            for i in len(q):
                el = q.popleft()
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
        return res



test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # ⁠         1
        # ⁠        / \
            # ⁠       3   2
        # ⁠      / \   \
            # ⁠     5   3   9
        In
        print(sol.largestValues())
