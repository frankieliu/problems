
Clean python solution

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/discuss/48908

* Lang:    python3
* Author:  hxuanz
* Votes:   3

Find Minimum in Rotated Sorted Array I----**no duplicate** ----O(logN)

    class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid
        return nums[lo] 

Find Minimum in Rotated Sorted Array II----**contain duplicates**----O(logN)~O(N)

    class Solution(object):
    def findMin(self, nums):
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + (hi -lo) / 2
            if nums[mid] > nums[hi]:
                lo = mid + 1
            else:
                hi = mid if nums[hi] != nums[mid] else hi - 1
        return nums[lo]
