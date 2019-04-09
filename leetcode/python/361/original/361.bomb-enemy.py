#
# @lc app=leetcode id=361 lang=python3
#
# [361] Bomb Enemy
#
# https://leetcode.com/problems/bomb-enemy/description/
#
# algorithms
# Medium (42.68%)
# Total Accepted:    32K
# Total Submissions: 74.9K
# Testcase Example:  '[["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]'
#
# Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0'
# (the number zero), return the maximum enemies you can kill using one bomb.
# The bomb kills all the enemies in the same row and column from the planted
# point until it hits the wall since the wall is too strong to be destroyed.
# Note: You can only put the bomb at an empty cell.
# 
# Example:
# 
# 
# 
# Input: [["0","E","0","0"],["E","0","W","E"],["0","E","0","0"]]
# Output: 3 
# Explanation: For the given grid,
# 
# 0 E 0 0 
# E 0 W E 
# 0 E 0 0
# 
# Placing a bomb at (1,1) kills 3 enemies.
# 
# 
#
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        
