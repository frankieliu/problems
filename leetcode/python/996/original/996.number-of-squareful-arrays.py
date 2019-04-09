#
# @lc app=leetcode id=996 lang=python3
#
# [996] Number of Squareful Arrays
#
# https://leetcode.com/problems/number-of-squareful-arrays/description/
#
# algorithms
# Hard (47.29%)
# Total Accepted:    3.7K
# Total Submissions: 7.8K
# Testcase Example:  '[1,17,8]'
#
# Given an array A of non-negative integers, the array is squareful if for
# every pair of adjacent elements, their sum is a perfect square.
# 
# Return the number of permutations of A that are squareful.  Two permutations
# A1 and A2 differ if and only if there is some index i such that A1[i] !=
# A2[i].
# 
# 
# 
# Example 1:
# 
# 
# Input: [1,17,8]
# Output: 2
# Explanation: 
# [1,8,17] and [17,8,1] are the valid permutations.
# 
# 
# Example 2:
# 
# 
# Input: [2,2,2]
# Output: 1
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 12
# 0 <= A[i] <= 1e9
# 
#
class Solution:
    def numSquarefulPerms(self, A: List[int]) -> int:
