"""704. Binary Search

Given a sorted (in ascending order) integer array nums of n elements
and a target value, write a function to search target in nums. If
target exists, then return its index, otherwise return -1.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
"""

class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.help(nums, 0, len(nums) - 1, target)

    def help(self, nums, i, j, target):
        if i > j:
            return -1
        l2 = (j + i) // 2
        print(i, j, l2)

        if nums[l2] == target:
            return l2

        if nums[l2] > target:
            return self.help(nums, i, l2-1, target)
        else:
            return self.help(nums, l2+1, j, target)


if __name__ == "__main__":
    s = Solution()
    nums = [-1,0,3,5,9,12]
    target = 9
    print(s.search(nums, target))
    # Output: 4
    nums = [-1,0,3,5,9,12]
    target = 2
    print(s.search(nums, target))
