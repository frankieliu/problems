"""34. Find First and Last Position of Element in Sorted Array
Medium

1199

64

Favorite

Share

Given an array of integers nums sorted in ascending order, find the
starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Accepted
251.1K
Submissions
769.7K
"""
class Solution:

    def searchRange(self, a, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(a) == 0:
            return [-1, -1]

        hi = self.firstGreaterThan(a, target)

        if hi == 0 or a[hi-1] != target:
            return [-1, -1]
        print(hi)

        lo = self.firstGreaterThan(a, target-1)
        return [lo, hi-1]

    def firstGreaterThan(self, a, target):
        lo = 0
        hi = len(a) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] <= target:
                lo = mid + 1
            else:
                hi = mid
        if hi == len(a)-1 and a[hi] == target:
            return len(a)
        else:
            return hi


"""
    0 1 2 3 4 5
          *
          3 4 5
            m
          3 4
          m
"""

s = Solution()

print(s.firstGreaterThan([0, 1, 2, 2, 2, 2, 3, 4, 5], 2))
print(s.searchRange([0, 1, 2, 2, 2, 2, 3, 4, 5], 2))
print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
