#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
#
# https://leetcode.com/problems/binary-tree-postorder-traversal/description/
#
# algorithms
# Hard (46.35%)
# Total Accepted:    229.5K
# Total Submissions: 495.1K
# Testcase Example:  '[1,null,2,3]'
#
# Given a binary tree, return the postorder traversal of its nodes' values.
#
# Example:
#
#
# Input: [1,null,2,3]
# ⁠  1
# ⁠   \
# ⁠    2
# ⁠   /
# ⁠  3
#
# Output: [3,2,1]
#
#
# Follow up: Recursive solution is trivial, could you do it iteratively?
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        """
        post is more tricky
        put root
        let's put a tag on root
        that is if you pop a None then
        it is the first time you are visiting a node
        if there is no tag then go ahead and print it
        """

        if root is None:
            return []
        tag = None
        s = []
        out = []
        s.append(root)
        s.append(tag)
        while s:
            t = s.pop()
            if t is tag:
                t = s.pop()
                s.append(t)
                if t.right:
                    s.append(t.right)
                    s.append(tag)
                if t.left:
                    s.append(t.left)
                    s.append(tag)
            else:
                out.append(t.val)
        return out


test = False
if test:
    from TreeNode.TreeNode import arrayToTreeNode, TreeNode
    tn = arrayToTreeNode([1, None, 2, 3])
    tmp = TreeNode(0)
    s = Solution()
    print(s.postorderTraversal(tn))
