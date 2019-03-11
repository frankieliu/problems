#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.com/problems/lru-cache/description/
#
# algorithms
# Hard (23.49%)
# Total Accepted:    250.8K
# Total Submissions: 1.1M
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
#
# Design and implement a data structure for Least Recently Used (LRU) cache. It
# should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key
# exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present.
# When the cache reached its capacity, it should invalidate the least recently
# used item before inserting a new item.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#
#

class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        out = []

        for i in range(0, capacity):
            out.append(TreeNode(("num{}".format(i), None)))

        for i in range(0, capacity):
            if i == 0:
                out[i].left = None
            else:
                out[i].left = out[i-1]
            if i == capacity - 1:
                out[i].right = None
            else:
                out[i].right = out[i+1]

        self.head = out[0]
        self.tail = out[-1]
        self.h = {}

    def print(self):
        if self.h:
            print("Hash:", end=" ")
            for k, v in self.h.items():
                print((k, v.val), end=" ")
        if self.head:
            print("Tree:", end=" ")
            t = self.head
            while t:
                left = t.left.val if t.left else None
                right = t.right.val if t.right else None
                print("({}, {}, {})".format(left, t.val, right), end=" ")
                t = t.right
        print()


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.h:
            return(self.insert_head(key))
        else:
            return -1

    def insert_head(self, key):
        """
        save the node left and right
        put the node at head and change left's right and right's left
        """
        # Get the node from the key
        node = self.h[key]

        if node != self.head:
            left = node.left
            right = node.right
            head = self.head

            if left:
                left.right = right
            if right:
                right.left = left

            node.left = None
            node.right = head
            head.left = node
            self.head = node

            if node == self.tail:
                self.tail = left

        return self.head.val[1]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.get(key) != -1:

            self.head.val = (key,value)

        else:
            node = TreeNode((key,value))
            node.left = None
            node.right = self.head
            self.head.left = node
            self.head = node

            if self.tail.val[0] in self.h:
                del self.h[self.tail.val[0]]
            self.tail = self.tail.left
            self.tail.right = None

            self.h[self.head.val[0]] = self.head

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

test = False
if test:
    from TreeNode.TreeNode import TreeNode

    print("Creating LRU")
    lr = LRUCache(1)
    lr.print()

    print("Adding 2,1")
    lr.put(2, 1)
    lr.print()

    print("Getting 1")
    print(lr.get(1))
    lr.print()

    if False:
        print("Getting 1")
        print(lr.get(1))
        lr.print()

        print("Adding 3")
        lr.put(3, 3)
        lr.print()

        print("Getting 2")
        print(lr.get(2))
        lr.print()

        print("Putting 4")
        lr.put(4, 4)
        lr.print()

        print("Getting 1")
        print(lr.get(1))
        lr.print()

        print("Getting 3")
        print(lr.get(3))
        lr.print()

        print("Getting 4")
        print(lr.get(4))
        lr.print()
