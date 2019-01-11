"""47. Permutations II
Medium

762

39

Favorite

Share
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
Accepted
209,929
Submissions
547,120"""

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = []
        self.helper(nums, 0, out)
        return out

    def helper(self, nums, i, out):
        if i == len(nums)-1:
            out.append(nums[:])
            return
        h = set()
        for j in range(i, len(nums)):
            if i != j and (nums[i] == nums[j] or nums[j] in h):
                continue
            h.add(nums[j])
            # print(h)
            nums[i], nums[j] =  nums[j], nums[i]
            self.helper(nums, i+1, out)
            nums[i], nums[j] =  nums[j], nums[i]

s = Solution()
print(s.permuteUnique([2, 2, 1, 1]))
