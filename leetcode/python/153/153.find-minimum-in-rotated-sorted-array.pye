#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (42.32%)
# Total Accepted:    253K
# Total Submissions: 597.9K
# Testcase Example:  '[3,4,5,1,2]'
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown
# to you beforehand.
#
# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).
#
# Find the minimum element.
#
# You may assume no duplicate exists in the array.
#
# Example 1:
#
#
# Input: [3,4,5,1,2]
# Output: 1
#
#
# Example 2:
#
#
# Input: [4,5,6,7,0,1,2]
# Output: 0
#
#
#
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.help(nums, 0, len(nums))

    def help(self, nums, i, j):
        print(nums[i:j])
        if (j-i) == 0:
            return None
        if (j-i) == 1:
            return nums[i]
        if (j-i) == 2:
            return min(nums[i], nums[i+1])
        mid = (j+i) // 2
        if nums[mid] >= nums[j-1]:
            return self.help(nums, mid+1, j)
        else:
            return self.help(nums, i, mid+1)


test = False
if test:
    s = Solution()
    print(s.findMin([4,5,1,2,3,4]))
