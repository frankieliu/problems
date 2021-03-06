#
# @lc app=leetcode id=209 lang=python3
#
# [209] Minimum Size Subarray Sum
#
# https://leetcode.com/problems/minimum-size-subarray-sum/description/
#
# algorithms
# Medium (34.03%)
# Total Accepted:    158.4K
# Total Submissions: 465.3K
# Testcase Example:  '7\n[2,3,1,2,4,3]'
#
# Given an array of n positive integers and a positive integer s, find the
# minimal length of a contiguous subarray of which the sum ≥ s. If there isn't
# one, return 0 instead.
#
# Example: 
#
#
# Input: s = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: the subarray [4,3] has the minimal length under the problem
# constraint.
#
# Follow up:
#
# If you have figured out the O(n) solution, try coding another solution of
# which the time complexity is O(n log n). 
#
#
class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 0 if nums[0] < s else 1

        # find the first sum that is over s
        i, j = 0, 0
        curr = 0
        while curr < s and j < len(nums):
            curr += nums[j]
            j += 1
        # j is not inclusive

        # elements too small
        if curr < s:
            return 0

        # remove elements looking for smaller subarray
        while curr - nums[i] >= s:
            curr -= nums[i]
            i += 1

        min_len = j-i
        if j == len(nums):
            return min_len

        while True:
            # shift to right
            curr += - nums[i] + nums[j]
            i, j = i+1, j+1

            # remove elements looking for smaller subarray
            while curr-nums[i] >= s:
                curr -= nums[i]
                i += 1

            if j-i < min_len:
                min_len = j-i

            if j == len(nums):
                break

        return min_len

test = True
if test:
    s = Solution()
    ss = 11
    nums = [1,2,3,4,5]
    # Output: 2
    print(s.minSubArrayLen(ss, nums))
