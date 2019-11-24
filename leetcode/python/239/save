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
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums, k):
        # break up into windows of size k
        # create two cum sum
        if len(nums) == 0:
            return []
        if len(nums) <= k:
            return [max(nums)]
        ln = len(nums)
        infn = -(1<<31)
        nums += [infn] * (k - (ln % k))
        maxl, maxr, leftcs, rightcs = infn, infn, [infn]*len(nums), [infn]*len(nums)
        for i in range(0, len(nums)):
            if i % k == 0:
                maxl = infn
                maxr = infn
            j = len(nums) - i - 1
            maxl = max(maxl, nums[i])
            maxr = max(maxr, nums[j])
            leftcs[i] = maxl
            rightcs[j] = maxr
        # print(leftcs, rightcs)
        # [1, 3, 3]   [-3, 5, 5]  [6, 7, 7]
        # [3, 3, -1]  [5, 5, 3]   [7, 7, -2147483648]
        return [max(rightcs[i],leftcs[i+k-1]) for i in range(0,ln-k+1)]


test = True
if test:
    s = Solution()
    case = [False]*1 + [True] + [False]*1
    if case[0]:
        # Example:
        nums = [1,3,-1,-3,5,3,6,7]
        k = 3
        # Output: [3,3,5,5,6,7]
        print(s.maxSlidingWindow(nums, k))
    if case[1]:
        # Example:
        nums = []
        k = 3
        # Output: [3,3,5,5,6,7]
        print(s.maxSlidingWindow(nums, k))
