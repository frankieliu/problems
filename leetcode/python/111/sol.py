
My solution in python

https://leetcode.com/problems/minimum-depth-of-binary-tree/discuss/36094

* Lang:    python3
* Author:  songzy12
* Votes:   27

The idea is to use recursion, the accepted short python code looks like follows:

    class Solution:
        # @param root, a tree node
        # @return an integer    
        def minDepth(self, root):
            if root == None:
                return 0
            if root.left==None or root.right==None:
                return self.minDepth(root.left)+self.minDepth(root.right)+1
            return min(self.minDepth(root.right),self.minDepth(root.left))+1
