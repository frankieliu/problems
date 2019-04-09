#
# @lc app=leetcode id=259 lang=python3
#
# [259] 3Sum Smaller
#
# https://leetcode.com/problems/3sum-smaller/description/
#
# algorithms
# Medium (44.44%)
# Total Accepted:    48.1K
# Total Submissions: 108.2K
# Testcase Example:  '[-2,0,1,3]\n2'
#
# Given an array of n integers nums and a target, find the number of index
# triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] +
# nums[j] + nums[k] < target.
# 
# Example:
# 
# 
# Input: nums = [-2,0,1,3], and target = 2
# Output: 2 
# Explanation: Because there are two triplets which sums are less than
# 2:
# [-2,0,1]
# ⁠            [-2,0,3]
# 
# 
# Follow up: Could you solve it in O(n^2) runtime?
# 
#
class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
