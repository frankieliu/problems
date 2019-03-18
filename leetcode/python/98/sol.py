
Python version based on inorder traversal

https://leetcode.com/problems/validate-binary-search-tree/discuss/32153

* Lang:    python3
* Author:  Google
* Votes:   36

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        # @param root, a tree node
        # @return a boolean
        # 7:38
        def isValidBST(self, root):
            output = []
            self.inOrder(root, output)
            
            for i in range(1, len(output)):
                if output[i-1] >= output[i]:
                    return False
    
            return True
    
        def inOrder(self, root, output):
            if root is None:
                return
            
            self.inOrder(root.left, output)
            output.append(root.val)
            self.inOrder(root.right, output)
