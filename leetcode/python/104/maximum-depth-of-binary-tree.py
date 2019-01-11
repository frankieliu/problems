"""104. Maximum Depth of Binary Tree
Easy

1029

43

Favorite

Share
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.

Accepted
424,595
Submissions
728,844"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        s = [(root, depth)]
        max_d = 0

        while s:
            n = s.pop()
            if n[0] is None:
                if n[1] > max_d:
                    max_d = n[1]
            else:
                s.append((n[0].left, n[1] + 1))
                s.append((n[0].right, n[1] + 1))

        return max_d
