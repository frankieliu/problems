
Python 1-line Dict Serialization

https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/discuss/248106

* Lang:    python3
* Author:  joinyoung
* Votes:   0

Somehow, at the very beginning, I thought it required me to serialize the tree into a string. Later on, I realized a dict or a list was OK, too. 
My solution is pretty much like what you could see in a .json file. Very Intuitive.
```
class Codec:
    def serialize(self, root):
        return {\'value\': root.val, \'children\': [self.serialize(child) for child in root.children]} if root else {}

    def deserialize(self, data):
        return Node(data[\'value\'], [self.deserialize(child) for child in data[\'children\']]) if data else None
```
