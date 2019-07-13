#
# @lc app=leetcode id=829 lang=python3
#
# [829] Consecutive Numbers Sum
#
# https://leetcode.com/problems/consecutive-numbers-sum/description/
#
# algorithms
# Hard (31.74%)
# Total Accepted:    8.4K
# Total Submissions: 26.5K
# Testcase Example:  '5'
#
# Given a positive integer N, how many ways can we write it as a sum of
# consecutive positive integers?
#
# Example 1:
#
#
# Input: 5
# Output: 2
# Explanation: 5 = 5 = 2 + 3
#
# Example 2:
#
#
# Input: 9
# Output: 3
# Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4
#
# Example 3:
#
#
# Input: 15
# Output: 4
# Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5
#
# Note: 1 <= N <= 10 ^ 9.
#
#
from math import sqrt

class Solution:
    def consecutiveNumbersSum(self, N):
        """
        N = x + (x + 1) + (x + n-1)
            x * n + n*(n-1)/2

        so N - n(n-1)/2 = xn
        or N - n(n-1)/2 is a multiple of n

        Constraints:

        the smallest n is 1
        the largest n is the one that has x = 1 or
        N = n*(n-1)/2 + n
        """

        count = 0
        # nmax = int(-1 + sqrt(1+8*N)/2)
        # print(nmax)
        n = 1
        n2 = n*(n-1)/2 + n
        while n2 <= N:
            if (N-n2) % n == 0:
                # print(n)
                count += 1
            n += 1
            n2 = n*(n-1)/2 + n

        # Note N-(n2-n) % n == N-n2 % n
        return count


test = True
if test:
    s = Solution()
    case = [False]*2 + [True] + [False]*3
    if case[0]:
        # Example 1:
        Input = 5
        # Output: 2
        print(s.consecutiveNumbersSum(Input))
    if case[1]:
        # Example 2:
        Input = 9
        # Output: 3
        print(s.consecutiveNumbersSum(Input))
    if case[2]:
        # Example 3:
        Input = 15
        # Output: 4
        print(s.consecutiveNumbersSum(Input))
