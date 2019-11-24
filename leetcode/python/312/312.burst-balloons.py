#
# @lc app=leetcode id=312 lang=python3
#
# [312] Burst Balloons
#
# https://leetcode.com/problems/burst-balloons/description/
#
# algorithms
# Hard (45.95%)
# Total Accepted:    55.5K
# Total Submissions: 120.9K
# Testcase Example:  '[3,1,5,8]'
#
# Given n balloons, indexed from 0 to n-1. Each balloon is painted with a
# number on it represented by array nums. You are asked to burst all the
# balloons. If the you burst balloon i you will get nums[left] * nums[i] *
# nums[right] coins. Here left and right are adjacent indices of i. After the
# burst, the left and right then becomes adjacent.
#
# Find the maximum coins you can collect by bursting the balloons wisely.
#
# Note:
#
#
# You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can
# not burst them.
# 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
#
#
# Example:
#
#
# Input: [3,1,5,8]
# Output: 167
# Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  -->
# []
# coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
#
#
class Solution:
    def maxCoins(self, n):
        """
        :type nums: List[int]
        :rtype: int
        """

        # treat the edges as the rest, and allow popping of edge
        # balloons
        n = [1] + n + [1]

        nn = len(n)

        # all possible pairs of boundaries
        dp = [[0]*nn for x in range(nn)]

        # The main idea is to think backwards, i.e. what is the
        # last ballon to burst, and how much that will yield
        #
        # The last ballon will burts in the following way
        # 1--Last Ballon--1
        #
        # where 1 is the just fences around the ballons,
        # 1 works well becaues 1*N*1 = N
        #
        # since this is the last ballon, then that allows us
        # to create a new fence at
        # 1 -- next ballon -- last ballon -- next ballon -- 1
        #
        # basically there are two subproblems now

        # DP means the maximum score having boundaries at i and i+2
        # where we don't count the boundaries as ballons, either
        # 1. they have already popped in the future or
        # 2. they are boundary ballons

        # Note below the two boundaries do not need to be popped,
        # the two boundaries will be popped in the future, so
        # dp[i][i+2] will only pop the i+1 th baloon
        for i in range(0, nn-2):
            dp[i][i+2] = n[i] * n[i+1] * n[i+2]
        print(dp)

        # Similarly when we consider dp[i][i+3] we will
        # consider both scenarios popping i+1/i+2, or
        # i+2/i+1, both of them dependent on
        # dp[i][i+2] if you pop i+2 first and
        # dp[i+1][i+3] if you pop i+1 first

        # now we increase the separation
        # we already did sep 2 then we need to find up to n-1 separation
        # for the final solution, we build bottom up

        for sep in range(3, nn):
            for i in range(0, nn-sep):
                j = i + sep
                # possible middle ballons to pop last
                cur = 0
                for k in range(i+1, j):
                    cur = max(
                        cur,
                        (n[i]*n[k]*n[j] +          # last balloon
                         dp[i][k] +                # left ballons
                         dp[k][j]))                # right ballons
                dp[i][j] = cur
        # return for the 1--1 balloons at the periphery
        return dp[0][nn-1]


test = True
if test:
    s = Solution()
    a = [3, 1, 5, 8]
    print(s.maxCoins(a))
