
Easy Python solution with comments

https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/discuss/74563

* Lang:    python3
* Author:  Nazariy
* Votes:   1

    # Definition for a binary tree node.
    # class TreeNode(object):
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution(object):
        def longestConsecutive(self, root):
            """
            :type root: TreeNode
            :rtype: int
            """
            #If it's empty then return 0 
            if root == None:
                return 0
            max_consecutive = self.traverse(root, None, 1)
            return max_consecutive
            
        """
        root is the current node
        prev_val is the previous value
        consecuive_num is the number of consecutive times  
        """
        def traverse(self, root, prev_val, consecutive_num):
            #Return the last consecutive number if the root is null
            if root == None:
                return consecutive_num
            
            new_consecutive = 1
            #The check is there because we initiall set pre_val to None
            if prev_val != None:
                if root.val == prev_val + 1:
                    #Overrrid the new_consecutive if the node is a consecutive node 
                    new_consecutive = (consecutive_num + 1)
    
            #Return max of either current consecutive, or the max of the left tree, or the right tree
            return max(consecutive_num, self.traverse(root.left, root.val, new_consecutive), self.traverse(root.right, root.val, new_consecutive))
