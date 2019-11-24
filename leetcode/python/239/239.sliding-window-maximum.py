#
# @lc app=leetcode id=239 lang=python3
#
# [239] Sliding Window Maximum
#
# https://leetcode.com/problems/sliding-window-maximum/description/
#
# algorithms
# Hard (36.73%)
# Total Accepted:    132.1K
# Total Submissions: 359.7K
# Testcase Example:  '[1,3,-1,-3,5,3,6,7]\n3'
#
# Given an array nums, there is a sliding window of size k which is moving from
# the very left of the array to the very right. You can only see the k numbers
# in the window. Each time the sliding window moves right by one position.
# Return the max sliding window.
#
# Example:
#
#
# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
#
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
# ⁠1 [3  -1  -3] 5  3  6  7       3
# ⁠1  3 [-1  -3  5] 3  6  7       5
# ⁠1  3  -1 [-3  5  3] 6  7       5
# ⁠1  3  -1  -3 [5  3  6] 7       6
# ⁠1  3  -1  -3  5 [3  6  7]      7
#
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty
# array.
#
# Follow up:
# Could you solve it in linear time?
#
#
from typing import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        This is the 84ms solution

           [.. k ..]
        1. Find the max of the first k-window
        2. If the next value is larger than the max_value,
           obviously it is the next maxValue
        3. Otherwise, if nums[i] == max_value, then you
           need to recompute a new max
        """

        if len(nums) == 0:
            return []
        max_value = max(nums[:k])
        res = [max_value]
        for i in range(len(nums)-k):
            if nums[i+k] > max_value:
                max_value = nums[i+k]
            elif nums[i] == max_value:
                max_value = max(nums[i+1:i+k+1])
            res.append(max_value)
        return res


test = True
if test:
    s = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        nums = [1, 3, -1, -3, 5, 3, 6, 7]
        k = 3
        # Output: [3,3,5,5,6,7]
        print(s.maxSlidingWindow(nums, k))
    if case[1]:
        # Example:
        nums = []
        k = 3
        # Output: [3,3,5,5,6,7]
        print(s.maxSlidingWindow(nums, k))
