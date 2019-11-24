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
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None
    def __repr__(self):
        return ("(" +
                ",".join([
                    str(self.val),str(self.left),str(self.right),str(self.next and self.next.val)])+
                ")")

class Solution:
    def connect(self, root):
        if root is None:
            return root

        def children(r):
            while r is not None:
                for x in [r.left, r.right]:
                    if x:
                        yield x
                r = r.next
            yield None

        next_root = root
        while next_root:
            nc = children(next_root)
            curr = next_root = next(nc)
            while curr:
                curr.next = next(nc)
                curr = curr.next
        return root


test = True
if test:
    tn = {x: TreeLinkNode(x) for x in [1, 2, 3, 4, 5, 7]}
    tn[1].left = tn[2]
    tn[1].right = tn[3]
    tn[2].left = tn[4]
    tn[2].right = tn[5]
    tn[3].right = tn[7]
    s = Solution()
    print(s.connect(tn[1]))
