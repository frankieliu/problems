
Python Simple Trie O(k) Solution, Must see [Silently AC is the best!]

https://leetcode.com/problems/map-sum-pairs/discuss/107524

* Lang:    python3
* Author:  y5yeyey
* Votes:   0

```
class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = {}

class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}
        
    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        node = self.root
        i = 0
        while i < len(key):
            # add following nodes
            if key[i] not in node.next:
                node.next[key[i]] = Node()
            node = node.next[key[i]]
            # update existed key-value pair
            if key in self.keys:
                node.val += val - self.keys[key]
            else:
                node.val += val
            i += 1
        self.keys[key] = val
        
    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        node = self.root
        i = 0
        while i < len(prefix) and prefix[i] in node.next:
            node = node.next[prefix[i]]
            i += 1
        return node.val if i == len(prefix) else 0
```
