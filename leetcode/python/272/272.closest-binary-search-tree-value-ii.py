#
# @lc app=leetcode id=272 lang=python3
#
# [272] Closest Binary Search Tree Value II
#
# https://leetcode.com/problems/closest-binary-search-tree-value-ii/description/
#
# algorithms
# Hard (43.96%)
# Total Accepted:    34.1K
# Total Submissions: 77.6K
# Testcase Example:  '[4,2,5,1,3]\n3.714286\n2'
#
# Given a non-empty binary search tree and a target value, find k values in the
# BST that are closest to the target.
#
# Note:
#
#
# Given target value is a floating point.
# You may assume k is always valid, that is: k ≤ total nodes.
# You are guaranteed to have only one unique set of k values in the BST that
# are closest to the target.
#
#
# Example:
#
#
# Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
#
# ⁠   4
# ⁠  / \
# ⁠ 2   5
# ⁠/ \
# 1   3
#
# Output: [4,3]
#
# Follow up:
# Assume that the BST is balanced, could you solve it in less than O(n) runtime
# (where n = total nodes)?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "("+",".join([str(self.val), str(self.left), str(self.right)])+")"


class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        Key optimization: you
        1. keep a successor and a predecessor stack
        2. compare the successor and predecessor diff from target
        3. take min
        4. repeat

        """
        def right(s, fwd=1):
            if fwd == 1:
                return s.right
            else:
                return s.left

        def left(s, fwd=1):
            if fwd == 1:
                return s.left
            else:
                return s.right

        def getNext(s, fdir):
            top = s.pop()
            curr = fdir(top)
            while curr:
                s.append(curr)
                curr = fdir(curr, -1)
            return top.val

        def buildStacks(r, target):
            succ, pred = [], []
            while r:
                if r.val == target:
                    succ.append(r)
                    pred.append(r)
                    break
                elif r.val > target:
                    succ.append(r)
                    r = r.left
                else:
                    pred.append(r)
                    r = r.right
            return succ, pred

        succ,pred = buildStacks(root, target)

        res = []
        while k > 0:
            if not pred:
                res.append(getNext(succ, right))
            elif not succ:
                res.append(getNext(pred, left))
            else:
                sd, pd = succ[-1].val - target, target - pred[-1].val
                if sd < pd:
                    res.append(getNext(succ, right))
                else:
                    res.append(getNext(pred, left))
            k -= 1
        return res


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        root = [4, 2, 5, 1, 3]
        dq = deque()
        top = TreeNode(root[0])
        dq.append(top)
        right_done = True
        for i in range(1, len(root)):
            if right_done:
                el = dq.popleft()
                el.left = TreeNode(root[i])
                dq.append(el.left)
                right_done = False
            else:
                el.right = TreeNode(root[i])
                dq.append(el.right)
                right_done = True
        target = 3.714286
        k = 2
        # Output: [4,3]
        # print(top)
        print(sol.closestKValues(top, target, k))
