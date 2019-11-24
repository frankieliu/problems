#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#
# https://leetcode.com/problems/jump-game-ii/description/
#
# algorithms
# Hard (27.12%)
# Total Accepted:    149.4K
# Total Submissions: 551K
# Testcase Example:  '[2,3,1,1,4]'
#
# Given an array of non-negative integers, you are initially positioned at the
# first index of the array.
#
# Each element in the array represents your maximum jump length at that
# position.
#
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#
#
# Input: [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2.
# ⁠   Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Note:
#
# You can assume that you can always reach the last index.
#
#
class Solution:
    def jump(self, A):
        next_seg, target, jumps = (0, 0), len(A)-1, 0
        while not (next_seg[0] <= target <= next_seg[1]):
            next_seg = (next_seg[1]+1, max(i+A[i] for i in range(next_seg[0],next_seg[1]+1)))
            jumps += 1
        return jumps


test = True
if test:
    s = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        Input = [2,3,1,1,4]
        # Output: 2
        print(s.jump(Input))
