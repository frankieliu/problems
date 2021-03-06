#
# @lc app=leetcode id=280 lang=python3
#
# [280] Wiggle Sort
#
# https://leetcode.com/problems/wiggle-sort/description/
#
# algorithms
# Medium (60.64%)
# Total Accepted:    63.3K
# Total Submissions: 104.4K
# Testcase Example:  '[3,5,2,1,6,4]'
#
# Given an unsorted array nums, reorder it in-place such that nums[0] <=
# nums[1] >= nums[2] <= nums[3]....
#
# Example:
#
#
# Input: nums = [3,5,2,1,6,4]
# Output: One possible answer is [3,5,1,6,2,4]
#
#
class Solution:
    def wiggleSort(self, n):
        """
        Do not return anything, modify nums in-place instead.
        """
        less = True
        for i in range(1, len(n)):
            if less:
                if n[i-1] > n[i]:
                    n[i-1], n[i] = n[i], n[i-1]
            else:
                if n[i-1] < n[i]:
                    n[i-1], n[i] = n[i], n[i-1]
            less = not less
