
An easy Python solution

https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35223

* Lang:    python3
* Author:  Google
* Votes:   59

The idea is to find the root first, then recursively build each left and right subtree

    # Definition for a  binary tree node
    # class TreeNode:
    #     def __init__(self, x):
    #         self.val = x
    #         self.left = None
    #         self.right = None
    
    class Solution:
        # @param num, a list of integers
        # @return a tree node
        # 12:37
        def sortedArrayToBST(self, num):
            if not num:
                return None
    
            mid = len(num) // 2
    
            root = TreeNode(num[mid])
            root.left = self.sortedArrayToBST(num[:mid])
            root.right = self.sortedArrayToBST(num[mid+1:])
    
            return root
