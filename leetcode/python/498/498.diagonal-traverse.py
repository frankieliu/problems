#
# @lc app=leetcode id=498 lang=python3
#
# [498] Diagonal Traverse
#
# https://leetcode.com/problems/diagonal-traverse/description/
#
# algorithms
# Medium (44.80%)
# Total Accepted:    35.8K
# Total Submissions: 79.9K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# Given a matrix of M x N elements (M rows, N columns), return all elements of
# the matrix in diagonal order as shown in the below image.
# 
# 
# 
# Example:
# 
# 
# Input:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 
# Output:  [1,2,4,7,5,3,6,8,9]
# 
# Explanation:
# 
# 
# 
# 
# 
# Note:
# 
# The total number of elements of the given matrix will not exceed 10,000.
# 
#
class Solution:
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        