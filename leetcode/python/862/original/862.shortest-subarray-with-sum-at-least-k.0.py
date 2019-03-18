#
# @lc app=leetcode id=862 lang=python3
#
# [862] Shortest Subarray with Sum at Least K
#
# https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/description/
#
# algorithms
# Hard (21.48%)
# Total Accepted:    9.1K
# Total Submissions: 42.4K
# Testcase Example:  '[1]\n1'
#
# Return the length of the shortest, non-empty, contiguous subarray of A with
# sum at least K.
# 
# If there is no non-empty subarray with sum at least K, return -1.
# 
# 
# 
# 
# 
# 
# 
# Example 1:
# 
# 
# Input: A = [1], K = 1
# Output: 1
# 
# 
# 
# Example 2:
# 
# 
# Input: A = [1,2], K = 4
# Output: -1
# 
# 
# 
# Example 3:
# 
# 
# Input: A = [2,-1,2], K = 3
# Output: 3
# 
# 
# 
# 
# Note:
# 
# 
# 1 <= A.length <= 50000
# -10 ^ 5 <= A[i] <= 10 ^ 5
# 1 <= K <= 10 ^ 9
# 
# 
# 
# 
# 
#
class Solution:
    def shortestSubarray(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        
