"""78. Subsets
Medium

1540

40

Favorite

Share

Given a set of distinct integers, nums, return all possible subsets
(the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

"""

class Solution:
    def subsets(self, a):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(a) == 0:
            return [[]]
        if len(a) == 1:
            return [[], a]
        return (
            [[a[0]] + x
             for x in self.subsets(a[1::])] +
            self.subsets(a[1::])
            )


s = Solution()
print(s.subsets([1,2,3]))
