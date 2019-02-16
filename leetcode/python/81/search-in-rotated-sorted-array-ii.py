"""81. Search in Rotated Sorted Array II
Medium

519

252

Favorite

Share

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. If found in the array return
true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:

This is a follow up problem to Search in Rotated Sorted Array, where
nums may contain duplicates.

Would this affect the run-time complexity? How and why?
Accepted
153,148
Submissions
471,527

"""

class Solution:
    def search(self, n, t):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        left = 0
        right = len(n)

        # right doesn't include the index

        while left < right:
            mid = left + (right - left) // 2
            if n[mid] == t:
                return True

            if n[left] < n[mid]:

                if (n[left] <= t < n[mid]):
                    right = mid
                else:
                    left = mid + 1

            elif n[mid] < n[left]:

                if (n[mid] < t < n[left]):
                    left = mid + 1
                else:
                    right = mid

            else:
                left += 1

        return False



s = Solution()
print(s.search([2,5,6,0,0,1,2], 0))
