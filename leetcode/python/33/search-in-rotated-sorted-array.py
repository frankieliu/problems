"""33. Search in Rotated Sorted Array
Medium

1810

267

Favorite

Share
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Accepted
346.4K
Submissions
1.1M"""


class Solution:
    def search(self, a, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # search for the smallest
        lo = 0
        hi = len(a)-1

        # 10 11 12 1 2 3 4
        #          x
        # 10 11 12 1
        #     x
        #       12 1
        #        x

        while lo < hi:
            mid = (lo + hi) // 2
            if a[mid] > a[hi]:
                lo = mid + 1
            else:
                hi = mid

        smid = lo
        print(smid)

        lo = 0
        hi = len(a)-1

        while lo <= hi:
            mid = (lo + hi) // 2
            midrot = (mid + smid) % len(a)

            if a[midrot] == target:
                return midrot
            if a[midrot] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return -1

s = Solution()
print(s.search([3, 5, 1], 5))
