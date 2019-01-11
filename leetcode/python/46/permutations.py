"""46. Permutations
Medium

1518

40

Favorite

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
Accepted
318,476
Submissions
609,405"""

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        out = [];
        self.helper(nums, 0, out)
        return(out)

    def helper(self, nums, i, out):
        if i == len(nums)-1:
            out.append(nums[:])
            return
        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]
            self.helper(nums, i+1, out)
            nums[i], nums[j] = nums[j], nums[i]


s = Solution()
print(s.permute([1, 2, 3]))
