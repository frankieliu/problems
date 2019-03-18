
Short Python recursive solution - O(n)

https://leetcode.com/problems/path-sum/discuss/36360

* Lang:    python3
* Author:  Google
* Votes:   100

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        # @param root, a tree node
        # @param sum, an integer
        # @return a boolean
        # 1:27
        def hasPathSum(self, root, sum):
            if not root:
                return False
    
            if not root.left and not root.right and root.val == sum:
                return True
            
            sum -= root.val
    
            return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)
