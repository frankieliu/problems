#
# @lc app=leetcode id=673 lang=python3
#
# [673] Number of Longest Increasing Subsequence
#
# https://leetcode.com/problems/number-of-longest-increasing-subsequence/description/
#
# algorithms
# Medium (33.00%)
# Total Accepted:    26K
# Total Submissions: 78.8K
# Testcase Example:  '[1,3,5,4,7]'
#
# 
# Given an unsorted array of integers, find the number of longest increasing
# subsequence.
# 
# 
# Example 1:
# 
# Input: [1,3,5,4,7]
# Output: 2
# Explanation: The two longest increasing subsequence are [1, 3, 4, 7] and [1,
# 3, 5, 7].
# 
# 
# 
# Example 2:
# 
# Input: [2,2,2,2,2]
# Output: 5
# Explanation: The length of longest continuous increasing subsequence is 1,
# and there are 5 subsequences' length is 1, so output 5.
# 
# 
# 
# Note:
# Length of the given array will be not exceed 2000 and the answer is
# guaranteed to be fit in 32-bit signed int.
# 
#
class Solution:
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
