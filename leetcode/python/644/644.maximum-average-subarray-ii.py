#
# @lc app=leetcode id=644 lang=python3
#
# [644] Maximum Average Subarray II
#
# https://leetcode.com/problems/maximum-average-subarray-ii/description/
#
# algorithms
# Hard (28.01%)
# Total Accepted:    7.8K
# Total Submissions: 27.8K
# Testcase Example:  '[1,12,-5,-6,50,3]\n4'
#
# 
# Given an array consisting of n integers, find the contiguous subarray whose
# length is greater than or equal to k that has the maximum average value. And
# you need to output the maximum average value.
# 
# 
# 
# Example 1:
# 
# Input: [1,12,-5,-6,50,3], k = 4
# Output: 12.75
# Explanation:
# when length is 5, maximum average value is 10.8,
# when length is 6, maximum average value is 9.16667.
# Thus return 12.75.
# 
# 
# 
# 
# Note:
# 
# 1 k n 
# Elements of the given array will be in range [-10,000, 10,000].
# The answer with the calculation error less than 10^-5 will be accepted.
# 
# 
#
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
