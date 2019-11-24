#
# @lc app=leetcode id=1139 lang=python
#
# [1139] Largest 1-Bordered Square
#
# https://leetcode.com/problems/largest-1-bordered-square/description/
#
# algorithms
# Medium (42.11%)
# Total Accepted:    3.3K
# Total Submissions: 7.9K
# Testcase Example:  '[[1,1,1],[1,0,1],[1,1,1]]'
#
# Given a 2D grid of 0s and 1s, return the number of elements in the largest
# square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't
# exist in the grid.
# 
# 
# Example 1:
# 
# 
# Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
# Output: 9
# 
# 
# Example 2:
# 
# 
# Input: grid = [[1,1,0,0]]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= grid.length <= 100
# 1 <= grid[0].length <= 100
# grid[i][j] is 0 or 1
# 
#
class Solution(object):
    def largest1BorderedSquare(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
