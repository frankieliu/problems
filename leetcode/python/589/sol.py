
Anyone know why tail recursion isn't working?

https://leetcode.com/problems/n-ary-tree-preorder-traversal/discuss/259126

* Lang:    python3
* Author:  dlima
* Votes:   0

When I run the test case: 
```
{"$id":"1","children":[{"$id":"2","children":[{"$id":"3","children":[],"val":5}],"val":1}],"val":3}
```
It\'s output is correct:
```
[3,1,5]
```
but when I **submit** it says the output to that case is:
```
[1,3,5,6,2,4,3,1,5]
```

Here\'s my code for tail recursion:
```
class Solution(object):
    def preorder(self, node, traversal=[]):
        """
        :type node: Node
        :rtype: List[int]
        """
        if not node:
            return []
        
        traversal.extend([node.val])
        for child in node.children:
            self.preorder(child, traversal)
            
        return traversal
```

Here\'s the **same logic** with regular recursion that passes all tests:
```
class Solution(object):
    def preorder(self, node):
        """
        :type node: Node
        :rtype: List[int]
        """
        if not node:
            return []
        
        traversal = [node.val]
        for child in node.children:
            traversal.extend(self.preorder(child))
            
        return traversal
```
