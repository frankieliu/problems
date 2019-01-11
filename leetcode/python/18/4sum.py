"""18. 4Sum
Medium

819

157

Favorite

Share
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
Accepted
199.6K
Submissions
685.7K
"""

class Solution:

    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        # print(list(sorted(nums)))
        return self.nsum(4, 0, len(nums)-1, list(sorted(nums)), target)

    def nsum(self, n, i, j, nums, target):
        # print(">>", n, i, j, target)
        if j - i + 1 < n:
            return []

        out = []
        if n == 2:
            p1 = i
            p2 = j
            while p1 < p2:
                s = nums[p1] + nums[p2]
                if s == target:
                    out.append([nums[p1], nums[p2]])
                    p1 += 1
                    while p1 < p2 and nums[p1] == nums[p1-1]:
                        p1 += 1
                elif s < target:
                    p1 += 1
                else:
                    p2 -= 1
        else:
            for k in range(i, j+1):
                if k > i and nums[k] == nums[k-1]:
                    continue
                # print(k, nums[k], n-1, k+1, target, target-nums[k])
                a = self.nsum(n-1, k+1, j, nums, target-nums[k])
                if a:
                    # print([x + [nums[k]] for x in a])
                    out.extend([x + [nums[k]] for x in a])
                    # print("out", n, i, j, target, out)

        # print("Return: ", out)
        return out


s = Solution()
print(s.fourSum([-2, -1, 0, 0, 1, 2],0))
