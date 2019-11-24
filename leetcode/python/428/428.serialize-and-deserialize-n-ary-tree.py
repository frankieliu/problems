#
# @lc app=leetcode id=428 lang=python
#
# [428] Serialize and Deserialize N-ary Tree
#
# https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/description/
#
# algorithms
# Hard (52.66%)
# Total Accepted:    9K
# Total Submissions: 17.1K
# Testcase Example:  '{"$id":"1","children":[{"$id":"2","children":[{"$id":"5","children":[],"val":5},{"$id":"6","children":[],"val":6}],"val":3},{"$id":"3","children":[],"val":2},{"$id":"4","children":[],"val":4}],"val":1}'
#
# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
#
# Design an algorithm to serialize and deserialize an N-ary tree. An N-ary tree
# is a rooted tree in which each node has no more than N children. There is no
# restriction on how your serialization/deserialization algorithm should work.
# You just need to ensure that an N-ary tree can be serialized to a string and
# this string can be deserialized to the original tree structure.
#
# For example, you may serialize the following 3-ary tree
#
#
#
#
#
#
#
# as [1 [3[5 6] 2 4]]. You do not necessarily need to follow this format, so
# please be creative and come up with different approaches yourself.
#
#
#
# Note:
#
#
# N is in the range of  [1, 1000]
# Do not use class member/global/static variables to store states. Your
# serialize and deserialize algorithms should be stateless.
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
class Codec:
    """From yorkshire

    Serialize with preorder traversal where sentinel "#" indicates the
    final child of a node has been processed, so the function returns
    to its parent call.

    Deserialize by creating a deque (could also use an iterator with
    next() instead of popleft()).

    While the next item is not "#", create a child with the item, add
    the child to the list of children and recurse to create its
    subtree.

    Repeat until there are no more children, then ignore the "#".

    [1 [3 [5 6] 2 4]]

    let's try with this codec
    1 3 5 # 6 # #(3) 2 # 4 # #(1)


    Serialize
    if node is None:
       return
    add "root.val"
    for my children
       serialize(child)
    add "#"

    Deserialize
    create root

    helper:
    while not #:
      create child
      append child to root's children
      do child

    johnny puts node then number of children
    the you loop on the number of children

    """
    class Codec:
    def serialize(self, root):
        serial = []
        def preorder(node):
            if not node:
                return
            serial.append(str(node.val))
            for child in node.children:
                preorder(child)
            serial.append("#")      # indicates no more children, continue serialization from parent
        preorder(root)
        return " ".join(serial)

    def deserialize(self, data):
        if not data:
            return None
        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])
        def helper(node):
            if not tokens:
                return
            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)
            tokens.popleft()        # discard the "#"
        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
