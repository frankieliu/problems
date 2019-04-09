#
# @lc app=leetcode id=431 lang=python
#
# [431] Encode N-ary Tree to Binary Tree
#
# https://leetcode.com/problems/encode-n-ary-tree-to-binary-tree/description/
#
# algorithms
# Hard (61.32%)
# Total Accepted:    1.7K
# Total Submissions: 2.7K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Design an algorithm to encode an N-ary tree into a binary tree and decode the
# binary tree to get the original N-ary tree. An N-ary tree is a rooted tree in
# which each node has no more than N children. Similarly, a binary tree is a
# rooted tree in which each node has no more than 2 children. There is no
# restriction on how your encode/decode algorithm should work. You just need to
# ensure that an N-ary tree can be encoded to a binary tree and this binary
# tree can be decoded to the original N-nary tree structure.
# 
# For example, you may encode the following 3-ary tree to a binary tree in this
# way:
# 
# 
# 
# 
# 
# 
# 
# Note that the above is just an example which might or might not work. You do
# not necessarily need to follow this format, so please be creative and come up
# with different approaches yourself.
# 
# 
# 
# Note:
# 
# 
# N is in the range of  [1, 1000]
# Do not use class member/global/static variables to store states. Your encode
# and decode algorithms should be stateless.
# 
# 
#
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
"""
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
class Codec:

    def encode(self, root):
        """Encodes an n-ary tree to a binary tree.
        
        :type root: Node
        :rtype: TreeNode
        """
        

    def decode(self, data):
        """Decodes your binary tree to an n-ary tree.
        
        :type data: TreeNode
        :rtype: Node
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))
