#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (40.59%)
# Total Accepted:    185.8K
# Total Submissions: 457.6K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers, find the length of the longest
# consecutive elements sequence.
#
# Your algorithm should run in O(n) complexity.
#
# Example:
#
#
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
#
#
#
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)
        maxcount = 0

        while s:
            el = s.pop()
            count = 1

            # print("0: poped", el)
            # find all elements to the left
            tmp = el - 1
            while tmp in s:
                s.remove(tmp)
                count += 1
                # print("A: counting", tmp, count)
                tmp -= 1

            tmp = el + 1
            while tmp in s:
                s.remove(tmp)
                count += 1
                # print("B: counting", tmp, count)
                tmp += 1
            if count > maxcount:
                maxcount = count
        return maxcount


test = False
if test:
    s = Solution()
    print(s.longestConsecutive([100,4,200,1,3,2]))
