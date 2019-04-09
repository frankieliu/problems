#
# @lc app=leetcode id=250 lang=python3
#
# [250] Count Univalue Subtrees
#
# https://leetcode.com/problems/count-univalue-subtrees/description/
#
# algorithms
# Medium (47.95%)
# Total Accepted:    35.5K
# Total Submissions: 74K
# Testcase Example:  '[5,1,5,5,5,null,5]'
#
# Given a binary tree, count the number of uni-value subtrees.
#
# A Uni-value subtree means all nodes of the subtree have the same value.
#
# Example :
#
#
# Input:  root = [5,1,5,5,5,null,5]
#
# ⁠             5
# ⁠            / \
# ⁠           1   5
# ⁠          / \   \
# ⁠         5   5   5
#
# Output: 4
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
    def countUnivalSubtrees(self, root):
        def cus(root):
            if root is None:
                return 0, True    # count and isUni
            ll, iul = cus(root.left)
            rr, iur = cus(root.right)
            if ((iul and iur) and
                ((root.left is None or root.left.val == root.val) and
                 (root.right is None or root.right.val == root.val))):
                off = 1
                iu = True
            else:
                off = 0
                iu = False
            return ll+rr+off, iu
        count, _ = cus(root)
        return count


test = True
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    root = [5, 1, 5, 5, 5, None, 5]
    tn = arrayToTreeNode(root)
    tmp = TreeNode(0)
    s = Solution()
    print(s.countUnivalSubtrees(tn))
