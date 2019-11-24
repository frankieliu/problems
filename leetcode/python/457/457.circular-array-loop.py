#
# @lc app=leetcode id=457 lang=python
#
# [457] Circular Array Loop
#
# https://leetcode.com/problems/circular-array-loop/description/
#
# algorithms
# Medium (27.03%)
# Total Accepted:    13.7K
# Total Submissions: 50.7K
# Testcase Example:  '[2, -1, 1, 2, 2]'
#
# You are given an array of positive and negative integers. If a number n at an
# index is positive, then move forward n steps. Conversely, if it's negative
# (-n), move backward n steps. Assume the first element of the array is forward
# next to the last element, and the last element is backward next to the first
# element. Determine if there is a loop in this array. A loop starts and ends
# at a particular index with more than 1 element along the loop. The loop must
# be "forward" or "backward'.
# 
# Example 1: Given the array [2, -1, 1, 2, 2], there is a loop, from index 0 ->
# 2 -> 3 -> 0.
# 
# Example 2: Given the array [-1, 2], there is no loop.
# 
# Note: The given array is guaranteed to contain no element "0".
# 
# Can you do it in O(n) time complexity and O(1) space complexity?
# 
#
class Solution(object):
    def circularArrayLoop(self, nums: List[int]) -> bool:
        def jump(i,nums):
            res = (nums[i] + i) % len(nums)
            if res < 0:
                res += len(nums)
            return res
        for i in range(0,len(nums)):
            if nums[i] == 0:
                continue
            j = i
            k = jump(i,nums)
            while nums[i]*nums[k] > 0 and nums[i]*nums[jump(k,nums)] > 0:
                # print(j,k)
                if j == k:
                    if j == jump(j, nums):
                        break
                    return True
                j = jump(j,nums)
                k = jump(jump(k,nums),nums)
            # print("exited")
            j = i
            ni = nums[i]
            while ni*nums[j] > 0:
                k = jump(j,nums)
                nums[j] = 0
                j = k
            print(nums)
        return False
