#
# @lc app=leetcode id=634 lang=python3
#
# [634] Find the Derangement of An Array
#
# https://leetcode.com/problems/find-the-derangement-of-an-array/description/
#
# algorithms
# Medium (37.27%)
# Total Accepted:    4.6K
# Total Submissions: 12.3K
# Testcase Example:  '1'
#
# 
# In combinatorial mathematics, a derangement is a permutation of the elements
# of a set, such that no element appears in its original position.
# 
# 
# 
# There's originally an array consisting of n integers from 1 to n in ascending
# order, you need to find the number of derangement it can generate.
# 
# 
# 
# Also, since the answer may be very large, you should return the output mod
# 10^9 + 7.
# 
# 
# Example 1:
# 
# Input: 3
# Output: 2
# Explanation: The original array is [1,2,3]. The two derangements are [2,3,1]
# and [3,1,2].
# 
# 
# 
# Note:
# n is in the range of [1, 10^6].
# 
#
class Solution:
    def findDerangement(self, n: int) -> int:
        
