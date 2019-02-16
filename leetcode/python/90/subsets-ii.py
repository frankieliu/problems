"""90. Subsets II
Medium

728

39

Favorite

Share

Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

Accepted
183,549
Submissions
446,999

"""
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = sorted(nums)
        return self.help(n, 0)

    def help(self, nums, i):

        if i == len(nums):
            return [[]]
        if i == len(nums)-1:
            return [[], [nums[i]]]

        count = 1
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            count += 1
            j += 1

        out = []
        s = self.help(nums, j)
        # print(s)
        for j in range(0, count+1):
            out.extend([[nums[i]] * j + x for x in s])
        return out


s = Solution()
print(s.subsetsWithDup([1, 2, 2, 3, 3]))
