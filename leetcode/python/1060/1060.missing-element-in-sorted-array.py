#
# @lc app=leetcode id=1060 lang=python
#
# [1060] Missing Element in Sorted Array
#
# https://leetcode.com/problems/missing-element-in-sorted-array/description/
#
# algorithms
# Medium (53.92%)
# Total Accepted:    1.1K
# Total Submissions: 2.1K
# Testcase Example:  '[4,7,9,10]\n1'
#
# Given a sorted array A of unique numbers, find the K-th missing number
# starting from the leftmost number of the array.
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [4,7,9,10], K = 1
# Output: 5
# Explanation: 
# The first missing number is 5.
# 
# 
# Example 2:
# 
# 
# Input: A = [4,7,9,10], K = 3
# Output: 8
# Explanation: 
# The missing numbers are [5,6,8,...], hence the third missing number is 8.
# 
# 
# Example 3:
# 
# 
# Input: A = [1,2,4], K = 3
# Output: 6
# Explanation: 
# The missing numbers are [3,5,6,7,...], hence the third missing number is
# 6.
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# 1 <= A[i] <= 1e7
# 1 <= K <= 1e8
# 
#
class Solution(object):
    def missingElement(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
