
6-line simple Python solution using DFS

https://leetcode.com/problems/house-robber-iii/discuss/79458

* Lang:    python3
* Author:  feather
* Votes:   4

  The dfs function returns an array, the first element means the maximum if we include the value of the current node, and the second element means the maximum if we exclude the value of the current node.

  So in the return statement, as the first element, we include the value of the current node, and we should exclude the left and right children, so we add the second element from the result of left and right children. The second element has 4 conditions, we can include the left child and include the right child, include the left child and exclude the right child..., so we return the maximum of them.

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def rob(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            def dfs(node):
                if not node:
                    return [0, 0]
                left, right = dfs(node.left), dfs(node.right)
                return [node.val+left[1]+right[1], max([left[0]+right[0], left[0]+right[1], left[1]+right[0], left[1]+right[1]])]
            
            return max(dfs(root))
