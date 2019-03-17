
Easy python solution

https://leetcode.com/problems/minimum-absolute-difference-in-bst/discuss/99957

* Lang:    python3
* Author:  yang_fan
* Votes:   0

I first use stack to transversal the values of nodes, use another list to store all the values, sort the list and find the min distance between neighbor values.
```
class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:return None
        stack=[root]
        nodes=[]
        while stack:
            node=stack.pop()
            nodes.append(node.val)
            if not node.left and not node.right:
                continue
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        if len(set(nodes)!=len(nodes):return 0
        nodes.sort()
        dis=[]
        for i in range(len(nodes)-1):
            dis.append(abs(nodes[i]-nodes[i+1]))
        return min(dis)
```
