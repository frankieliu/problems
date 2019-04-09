#
# @lc app=leetcode id=573 lang=python3
#
# [573] Squirrel Simulation
#
# https://leetcode.com/problems/squirrel-simulation/description/
#
# algorithms
# Medium (53.14%)
# Total Accepted:    5.7K
# Total Submissions: 10.7K
# Testcase Example:  '5\n7\n[2,2]\n[4,4]\n[[3,0], [2,5]]'
#
# There's a tree, a squirrel, and several nuts. Positions are represented by
# the cells in a 2D grid. Your goal is to find the minimal distance for the
# squirrel to collect all the nuts and put them under the tree one by one. The
# squirrel can only take at most one nut at one time and can move in four
# directions - up, down, left and right, to the adjacent cell. The distance is
# represented by the number of moves.
# Example 1:
# 
# 
# Input: 
# Height : 5
# Width : 7
# Tree position : [2,2]
# Squirrel : [4,4]
# Nuts : [[3,0], [2,5]]
# Output: 12
# Explanation:
# ​​​​​
# 
# 
# Note:
# 
# 
# All given positions won't overlap.
# The squirrel can take at most one nut at one time.
# The given positions of nuts have no order.
# Height and width are positive integers. 3 <= height * width <= 10,000.
# The given positions contain at least one nut, only one tree and one
# squirrel.
# 
# 
#
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        
