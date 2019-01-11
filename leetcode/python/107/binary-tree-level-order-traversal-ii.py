"""107. Binary Tree Level Order Traversal II
Easy

571

98

Favorite

Share
Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]
Accepted
199,323
Submissions
443,947"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
from queue import Queue

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        d = Queue()
        out = []

        d.put((root, 0))

        while not d.empty():

            n = d.get()
            if n[0] is not None:
                if n[1] > len(out)-1:
                    out.append([])
                out[n[1]].append(n[0].val)
                d.put((n[0].left, n[1]+1))
                d.put((n[0].right, n[1]+1))

        return list(reversed(out))
