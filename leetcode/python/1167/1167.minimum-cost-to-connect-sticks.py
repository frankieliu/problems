#
# @lc app=leetcode id=1167 lang=python
#
# [1167] Minimum Cost to Connect Sticks
#
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/
#
# algorithms
# Medium (58.86%)
# Total Accepted:    2.4K
# Total Submissions: 4.1K
# Testcase Example:  '[2,4,3]'
#
# You have some sticks with positive integer lengths.
# 
# You can connect any two sticks of lengths X and Y into one stick by paying a
# cost of X + Y.  You perform this action until there is one stick remaining.
# 
# Return the minimum cost of connecting all the given sticks into one stick in
# this way.
# 
# 
# Example 1:
# Input: sticks = [2,4,3]
# Output: 14
# Example 2:
# Input: sticks = [1,8,3,5]
# Output: 30
# 
# 
# Constraints:
# 
# 
# 1 <= sticks.length <= 10^4
# 1 <= sticks[i] <= 10^4
# 
# 
#
class Solution(object):
    def connectSticks(self, sticks):
        """
        :type sticks: List[int]
        :rtype: int
        """
        
