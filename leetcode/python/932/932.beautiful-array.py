#
# @lc app=leetcode id=932 lang=python3
#
# [932] Beautiful Array
#
# https://leetcode.com/problems/beautiful-array/description/
#
# algorithms
# Medium (50.44%)
# Total Accepted:    3.4K
# Total Submissions: 6.7K
# Testcase Example:  '4'
#
# For some fixed N, an array A is beautiful if it is a permutation of the
# integers 1, 2, ..., N, such that:
# 
# For every i < j, there is no k with i < k < j such that A[k] * 2 = A[i] +
# A[j].
# 
# Given N, return any beautiful array A.  (It is guaranteed that one
# exists.)
# 
# 
# 
# Example 1:
# 
# 
# Input: 4
# Output: [2,1,4,3]
# 
# 
# 
# Example 2:
# 
# 
# Input: 5
# Output: [3,1,2,5,4]
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= N <= 1000
# 
# 
# 
# 
# 
#
class Solution:
    def beautifulArray(self, N):
        """
        :type N: int
        :rtype: List[int]
        """
        
