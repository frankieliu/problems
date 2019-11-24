#
# @lc app=leetcode id=1027 lang=python
#
# [1027] Longest Arithmetic Sequence
#
# https://leetcode.com/problems/longest-arithmetic-sequence/description/
#
# algorithms
# Medium (48.01%)
# Total Accepted:    8.9K
# Total Submissions: 18.5K
# Testcase Example:  '[3,6,9,12]'
#
# Given an array A of integers, return the length of the longest arithmetic
# subsequence in A.
#
# Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0
# <= i_1 < i_2 < ... < i_k <= A.length - 1, and that a sequence B is arithmetic
# if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).
#
#
#
# Example 1:
#
#
# Input: [3,6,9,12]
# Output: 4
# Explanation:
# The whole array is an arithmetic sequence with steps of length = 3.
#
#
#
# Example 2:
#
#
# Input: [9,4,7,2,10]
# Output: 3
# Explanation:
# The longest arithmetic subsequence is [4,7,10].
#
#
#
# Example 3:
#
#
# Input: [20,1,15,3,10,5,8]
# Output: 4
# Explanation:
# The longest arithmetic subsequence is [20,15,10,5].
#
#
#
#
#
# Note:
#
#
# 2 <= A.length <= 2000
# 0 <= A[i] <= 10000
#
#
#
from collections import defaultdict

class Solution(object):
    def longestArithSeqLength(self, a):
        """
        dp[i] is the LAS ending in i

        Since this will depend on the arithmetic sequence
        then keep a map for possible dp[i] depending on the
        arithmetic sequence that ends there
        """
        dp = [None] * len(a)
        for i in range(len(a)):
            dp[i] = defaultdict(int)

        res = 0
        for i in range(len(a)):
            for j in range(0, i):
                diff = a[i]-a[j]
                dp[i][diff] = dp[j][diff] + 1
                res = max(res, dp[i][diff])
        return res+1


test = True
if test:
    sol = Solution()
    case = [False]*1 + [True] + [False]*3
    if case[0]:
        # Example 1:
        Input = [3,6,9,12]
        # Output: 4
        print(sol.longestArithSeqLength(Input))
    if case[1]:
        # Example 2:
        Input = [9,4,7,2,10]
        # Output: 3
        print(sol.longestArithSeqLength(Input))
    if case[2]:
        # Example 3:
        Input = [20,1,15,3,10,5,8]
        # Output: 4
        print(sol.longestArithSeqLength(Input))
