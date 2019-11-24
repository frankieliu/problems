#
# @lc app=leetcode id=1121 lang=python
#
# [1121] Divide Array Into Increasing Sequences
#
# https://leetcode.com/problems/divide-array-into-increasing-sequences/description/
#
# algorithms
# Hard (52.57%)
# Total Accepted:    1.4K
# Total Submissions: 2.6K
# Testcase Example:  '[1,2,2,3,3,4,4]\n3'
#
# Given a non-decreasing array of positive integers nums and an integer K, find
# out if this array can be divided into one or more disjoint increasing
# subsequences of length at least K.
# 
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3,3,4,4], K = 3
# Output: true
# Explanation: 
# The array can be divided into the two subsequences [1,2,3,4] and [2,3,4] with
# lengths at least 3 each.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,6,6,7,8], K = 3
# Output: false
# Explanation: 
# There is no way to divide the array using the conditions required.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= K <= nums.length
# 1 <= nums[i] <= 10^5
# 
#
class Solution(object):
    def canDivideIntoSubsequences(self, nums, K):
        """
        :type nums: List[int]
        :type K: int
        :rtype: bool
        """
        
