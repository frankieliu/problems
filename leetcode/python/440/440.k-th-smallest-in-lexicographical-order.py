#
# @lc app=leetcode id=440 lang=python3
#
# [440] K-th Smallest in Lexicographical Order
#
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/description/
#
# algorithms
# Hard (26.08%)
# Total Accepted:    7.5K
# Total Submissions: 28.7K
# Testcase Example:  '13\n2'
#
# Given integers n and k, find the lexicographically k-th smallest integer in
# the range from 1 to n.
# 
# Note: 1 ≤ k ≤ n ≤ 10^9.
# 
# Example:
# 
# Input:
# n: 13   k: 2
# 
# Output:
# 10
# 
# Explanation:
# The lexicographical order is [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9], so
# the second smallest number is 10.
# 
# 
# 
#
class Solution:
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        
