
6 lines function body

https://leetcode.com/problems/house-robber-ii/discuss/59978

* Lang:    python3
* Author:  StefanPochmann
* Votes:   16

Standard solution, I guess, except I take a shortcut for the one-house case.

    class Solution:
        def rob(self, nums):
            def rob(nums):
                now = prev = 0
                for n in nums:
                    now, prev = max(now, prev + n), now
                return now
            return max(rob(nums[len(nums) != 1:]), rob(nums[:-1]))
