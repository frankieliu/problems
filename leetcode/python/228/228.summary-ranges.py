#
# @lc app=leetcode id=228 lang=python3
#
# [228] Summary Ranges
#
# https://leetcode.com/problems/summary-ranges/description/
#
# algorithms
# Medium (34.90%)
# Total Accepted:    121.5K
# Total Submissions: 348.2K
# Testcase Example:  '[0,1,2,4,5,7]'
#
# Given a sorted integer array without duplicates, return the summary of its
# ranges.
#
# Example 1:
#
#
# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
#
#
# Example 2:
#
#
# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
#
#
#
class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [str(nums[0])]

        beg = nums[0]
        last = nums[0]
        beg_idx = 0
        out = []
        for i in range(1, len(nums)):
            if nums[i] - beg == i - beg_idx:
                if i == len(nums) - 1:
                    out.append("{}->{}".format(beg, nums[i]))
            else:
                if beg != last:
                    out.append("{}->{}".format(beg, last))
                else:
                    out.append("{}".format(last))
                if i == len(nums) - 1:
                    out.append("{}".format(nums[i]))
                beg = nums[i]
                beg_idx = i
            last = nums[i]
        return out


test = True
if test:
    s = Solution()
    print(s.summaryRanges([0,2,3,4,5,7]))
