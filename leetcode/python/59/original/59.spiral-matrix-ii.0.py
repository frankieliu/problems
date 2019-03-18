#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#
# https://leetcode.com/problems/spiral-matrix-ii/description/
#
# algorithms
# Medium (44.92%)
# Total Accepted:    124.9K
# Total Submissions: 277.9K
# Testcase Example:  '3'
#
# Given a positive integer n, generate a square matrix filled with elements
# from 1 to n^2 in spiral order.
# 
# Example:
# 
# 
# Input: 3
# Output:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 8, 9, 4 ],
# ⁠[ 7, 6, 5 ]
# ]
# 
# 
#
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        
