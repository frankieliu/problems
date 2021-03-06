#
# @lc app=leetcode id=279 lang=python3
#
# [279] Perfect Squares
#
# https://leetcode.com/problems/perfect-squares/description/
#
# algorithms
# Medium (40.24%)
# Total Accepted:    156.5K
# Total Submissions: 388.8K
# Testcase Example:  '12'
#
# Given a positive integer n, find the least number of perfect square numbers
# (for example, 1, 4, 9, 16, ...) which sum to n.
#
# Example 1:
#
#
# Input: n = 12
# Output: 3
# Explanation: 12 = 4 + 4 + 4.
#
# Example 2:
#
#
# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.
#
class Solution:

    def numSquares(self, n):
        dp = [n for _ in range(0, n+1)]
        dp[0] = 0
        for i in range(1, n+1):
            dp[i] = min(dp[i-w*w] for w in range(1, int(i**0.5)+1)) + 1
        return dp[n]


test = True
if test:
    s = Solution()
    case = [False, True, False]
    if case[0]:
        # Input:
        n = 13
        print(s.numSquares(n))
    if case[1]:
        n = 112
        print(s.numSquares(n))
