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
    def jump(self, nums):
        if len(nums) == 1:
            return 0
        if max(nums) <= 1:
            return len(nums)-1

        index, count = 0, 0
        max_steps = len(nums) - 1

        # Nice insight:
        #
        # index is the current index I am standing in, and
        # it has the potential of reaching the largest index
        # since index + nums[index] was the maximum reacheable
        # amount from the previous jump
        #
        # for the next step among all the possible jumps, look
        # for some which will reach the furthest in the next step
        # i.e.
        #
        # for each of the possible 'next' indexes
        #  look for the one that will get us the furthest
        #  possible_next + A[possible_next] is max
        #  set index to possible_next and redo above


        # index + nums[index] is the maximum location that can be reached
        # loop till when we arrive the last element of nums;
        while index + nums[index] < max_steps:
         # if the nums[index] is 3, loop i from 1 to 3,
         # max is the max index we can arraive, next is the next step we will chose.
            Max, next = 0, 0
            for i in range(1, nums[index]+1):
                j = index + i
                step = nums[j]
                if step + i >= Max:
                    Max = step + i
                    next = j
            index = next
            count += 1

        return count + 1;


test = True
if test:
    s = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        Input = [2,3,1,1,4]
        # Output: 2
        print(s.jump(Input))
