#
# @lc app=leetcode id=356 lang=python3
#
# [356] Line Reflection
#
# https://leetcode.com/problems/line-reflection/description/
#
# algorithms
# Medium (30.75%)
# Total Accepted:    17.9K
# Total Submissions: 58.1K
# Testcase Example:  '[[1,1],[-1,1]]'
#
# Given n points on a 2D plane, find if there is such a line parallel to y-axis
# that reflect the given points.
# 
# Example 1:
# 
# 
# Input: [[1,1],[-1,1]]
# Output: true
# 
# 
# 
# Example 2:
# 
# 
# Input: [[1,1],[-1,-1]]
# Output: false
# 
# 
# Follow up:
# Could you do better than O(n^2) ?
#
class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        
