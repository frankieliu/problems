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
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        out = []
        q = deque()
        for i in range(len(nums)):
            el = nums[i]
            # top to queue is smaller
            # get rid of things that are older and smaller
            while q and nums[q[-1]] < el:
                q.pop()
            q.append(i)
            # bottom of queue has largest numbers
            if q[0] == i - k:
                q.popleft()
            out.append(nums[q[0]])
        # we need to begin with kth element
        return out[k - 1:]


test = True
if test:
    s = Solution()
    Example = [1, 3, -1, -3, 5, 3, 6, 7]
    print(s.maxSlidingWindow(Example, 3))
