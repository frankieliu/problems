"""15. 3Sum
Medium

2889

324

Favorite

Share

Given an array nums of n integers, are there elements a, b, c in nums
such that a + b + c = 0? Find all unique triplets in the array which
gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
Accepted
443,997
Submissions
1,956,828

"""

class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        slen = len(nums)
        if slen < 3:
            return []
        n = sorted(nums)
        out = []
        el = n[0] - 1  # just added for edge condition
        for i in range(0, slen-2):
            if n[i] == el:
                continue
            el = n[i]
            # search for things which sum to el
            lptr = i+1
            rptr = slen-1
            while lptr < rptr:
                nl = n[lptr]
                nr = n[rptr]
                s = nl + nr
                if s == -el:
                    out.append([el, nl, nr])
                    lptr += 1
                    while n[lptr] == nl and lptr < rptr:
                        lptr += 1
                elif s < -el:
                    lptr += 1
                else:
                    rptr -= 1
        return out
