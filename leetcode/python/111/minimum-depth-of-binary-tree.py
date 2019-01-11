"""111. Minimum Depth of Binary Tree
Easy

576

291

Favorite

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from
the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

Accepted
261,168
Submissions
756,069

"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from queue import Queue


class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root is None:
            return 0

        q = Queue()
        q.put(root)
        size = 1
        depth = 1

        while not q.empty():
            count = 0
            while size > 0:
                n = q.get()
                if n.left:
                    q.put(n.left)
                    count += 1
                if n.right:
                    q.put(n.right)
                    count += 1
                if n.left is None and n.right is None:
                    return depth
                size -= 1
            size = count
            depth += 1
