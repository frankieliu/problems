#
# @lc app=leetcode id=458 lang=python
#
# [458] Poor Pigs
#
# https://leetcode.com/problems/poor-pigs/description/
#
# algorithms
# Easy (44.62%)
# Total Accepted:    14.4K
# Total Submissions: 32.3K
# Testcase Example:  '1000\n15\n60'
#
# There are 1000 buckets, one and only one of them contains poison, the rest
# are filled with water. They all look the same. If a pig drinks that poison it
# will die within 15 minutes. What is the minimum amount of pigs you need to
# figure out which bucket contains the poison within one hour.
#
# Answer this question, and write an algorithm for the follow-up general case.
#
# Follow-up:
#
# If there are n buckets and a pig drinking poison will die within m minutes,
# how many pigs (x) you need to figure out the "poison" bucket within p
# minutes? There is exact one bucket with poison.
#
#
from math import ceil, log
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        return int(ceil(log(buckets)/log(minutesToTest//minutesToDie + 1)))


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*0
    print(sol.poorPigs(1000, 15, 60))
