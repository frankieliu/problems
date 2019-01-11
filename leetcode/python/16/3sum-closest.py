"""16. 3Sum Closest
Medium

809

62

Favorite

Share

Given an array nums of n integers and an integer target, find three
integers in nums such that the sum is closest to target. Return the
sum of the three integers. You may assume that each input would have
exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Accepted
225,119
Submissions
671,914

"""

class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        slen = len(nums)
        if slen < 3:
            return []
        n = sorted(nums)
        bsum = sum(nums[0:3])
        bdiff = abs(bsum - target)

        el = n[0] - 1  # just added for edge condition
        for i in range(0, slen-2):
            if n[i] == el:
                continue
            el = n[i]
            lptr = i+1
            rptr = slen-1
            while lptr < rptr:
                nl = n[lptr]
                nr = n[rptr]
                s = nl + nr + el
                if s == target:
                    return target
                elif s < target:
                    lptr += 1
                else:
                    rptr -= 1
                if abs(s - target) < bdiff:
                    bdiff = abs(s - target)
                    bsum = s

        return bsum


s = Solution()
print(s.threeSumClosest([1,2,5,10,11], 12))
