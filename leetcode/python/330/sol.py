
Simple 9-line Python Solution

https://leetcode.com/problems/patching-array/discuss/78498

* Lang:    python3
* Author:  myliu
* Votes:   8

    class Solution(object):
        def minPatches(self, nums, n):
            """
            :type nums: List[int]
            :type n: int
            :rtype: int
            """
            miss, i, added = 1, 0, 0
            while miss <= n:
                if i < len(nums) and nums[i] <= miss:
                    miss += nums[i]
                    i += 1
                else:
                    miss += miss
                    added += 1
            return added
