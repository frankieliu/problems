#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# https://leetcode.com/problems/largest-number/description/
#
# algorithms
# Medium (25.05%)
# Total Accepted:    117.8K
# Total Submissions: 470.5K
# Testcase Example:  '[10,2]'
#
# Given a list of non negative integers, arrange them such that they form the
# largest number.
#
# Example 1:
#
#
# Input: [10,2]
# Output: "210"
#
# Example 2:
#
#
# Input: [3,30,34,5,9]
# Output: "9534330"
#
#
# Note: The result may be very large, so you need to return a string instead of
# an integer.
#
#
import functools

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        """
        Note:
        33, 330
        """
        out = "".join(
            sorted([str(x) for x in nums],
                   key=functools.cmp_to_key(compare_concat)))
        out = out.lstrip("0")

        if out == "":
            return "0"
        return out


def compare_concat(a, b):
    return 1 if (a+b) < (b+a) else -1

test = True
if test:
    s = Solution()
    print(s.largestNumber([3, 30, 34, 5, 9]))
    # print(sorted(["30", "3"], key=functools.cmp_to_key(compare_concat)))
