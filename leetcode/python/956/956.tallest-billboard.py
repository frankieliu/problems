#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (36.31%)
# Total Accepted:    2.5K
# Total Submissions: 6.9K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height.  The
# billboard will have two steel supports, one on each side.  Each steel support
# must be an equal height.
# 
# You have a collection of rods which can be welded together.  For example, if
# you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
# 
# Return the largest possible height of your billboard installation.  If you
# cannot support the billboard, return 0.
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
# 
# 
# 
# Example 2:
# 
# 
# Input: [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
# 
# 
# 
# 
# Example 3:
# 
# 
# Input: [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
# 
# 
# 
# 
# 
# Note:
# 
# 
# 0 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# The sum of rods is at most 5000.
# 
# 
#
class Solution:
    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        
