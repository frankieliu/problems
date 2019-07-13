#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# https://leetcode.com/problems/find-the-duplicate-number/description/
#
# algorithms
# Medium (47.85%)
# Total Accepted:    159.2K
# Total Submissions: 332.6K
# Testcase Example:  '[1,3,4,2,2]'
#
# Given an array nums containing n + 1 integers where each integer is between 1
# and n (inclusive), prove that at least one duplicate number must exist.
# Assume that there is only one duplicate number, find the duplicate one.
#
# Example 1:
#
#
# Input: [1,3,4,2,2]
# Output: 2
#
#
# Example 2:
#
#
# Input: [3,1,3,4,2]
# Output: 3
#
# Note:
#
#
# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n^2).
# There is only one duplicate number in the array, but it could be repeated
# more than once.
#
#
#
class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = 0
        f = 0
        while True:
                s = nums[s]
                f = nums[nums[f]]
                if s == f:
                    break
        s = 0
        while s != f:
            s = nums[s]
            f = nums[f]
        return s


test = True
if test:
    s = Solution()
    case = [True] * 2
    if case[0]:
        # Example 1:
        Input = [1,3,4,2,2]
        # Output: 2
        print(s.findDuplicate(Input))
    if case[1]:
        # Example 2:
        Input = [3,1,3,4,2]
        # Output: 3
        print(s.findDuplicate(Input))
