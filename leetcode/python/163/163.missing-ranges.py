#
# @lc app=leetcode id=163 lang=python3
#
# [163] Missing Ranges
#
# https://leetcode.com/problems/missing-ranges/description/
#
# algorithms
# Medium (22.96%)
# Total Accepted:    52.2K
# Total Submissions: 227.3K
# Testcase Example:  '[0,1,3,50,75]\n0\n99'
#
# Given a sorted integer array nums, where the range of elements are in the
# inclusive range [lower, upper], return its missing ranges.
#
# Example:
#
#
# Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
# Output: ["2", "4->49", "51->74", "76->99"]
#
#
#
class Solution:
    def findMissingRanges(self, nums, lower, upper):
        out = []
        nums.append(upper+1)
        a = [lower-1] + nums
        for i in range(0, len(a)-1):
            if a[i+1] - a[i] == 2:
                out.append(str(a[i]+1))
            elif a[i+1] - a[i] > 2:
                out.append("{}->{}".format(a[i]+1, a[i+1]-1))
        return out


test = True
if test:
    s = Solution()
    nums = [0, 1, 3, 50, 75]
    lower = 0
    upper = 99
    print(s.findMissingRanges(nums, lower, upper))
