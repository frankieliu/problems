#
# @lc app=leetcode id=659 lang=python3
#
# [659] Split Array into Consecutive Subsequences
#
# https://leetcode.com/problems/split-array-into-consecutive-subsequences/description/
#
# algorithms
# Medium (39.45%)
# Total Accepted:    16.9K
# Total Submissions: 42.8K
# Testcase Example:  '[1,2,3,3,4,5]'
#
# You are given an integer array sorted in ascending order (may contain
# duplicates), you need to split them into several subsequences, where each
# subsequences consist of at least 3 consecutive integers. Return whether you
# can make such a split.
# 
# Example 1:
# 
# Input: [1,2,3,3,4,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3
# 3, 4, 5
# 
# 
# 
# Example 2:
# 
# Input: [1,2,3,3,4,4,5,5]
# Output: True
# Explanation:
# You can split them into two consecutive subsequences : 
# 1, 2, 3, 4, 5
# 3, 4, 5
# 
# 
# 
# Example 3:
# 
# Input: [1,2,3,4,4,5]
# Output: False
# 
# 
# 
# Note:
# 
# The length of the input is in range of [1, 10000]
# 
# 
#
class Solution:
    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
