#
# @lc app=leetcode id=935 lang=python3
#
# [935] Knight Dialer
#
# https://leetcode.com/problems/knight-dialer/description/
#
# algorithms
# Medium (37.15%)
# Total Accepted:    6.1K
# Total Submissions: 16.3K
# Testcase Example:  '1'
#
# A chess knight can move as indicated in the chess diagram below:
#
# .           
#
#
#
# This time, we place our chess knight on any numbered key of a phone pad
# (indicated above), and the knight makes N-1 hops.  Each hop must be from one
# key to another numbered key.
#
# Each time it lands on a key (including the initial placement of the knight),
# it presses the number of that key, pressing N digits total.
#
# How many distinct numbers can you dial in this manner?
#
# Since the answer may be large, output the answer modulo 10^9 + 7.
#
#
#
#
#
#
#
# Example 1:
#
#
# Input: 1
# Output: 10
#
#
#
# Example 2:
#
#
# Input: 2
# Output: 20
#
#
#
# Example 3:
#
#
# Input: 3
# Output: 46
#
#
#
#
# Note:
#
#
# 1 <= N <= 5000
#
#
#
#
#
#
class Solution:
    def knightDialer(self, N):
        g={
            1: [6,8],
            2: [7,9],
            3: [4,8],
            4: [3,9,0],
            5: [],
            6: [1,7,0],
            7: [2,6],
            8: [1,3],
            9: [2,4],
            0: [4,6]
        }
        # dp stores the number of ending in i
        for i in range(1,length+1):
            for n in [0,1,2,3,4,5,6,7,8,9]:
                for k in g[start]:
                dpa = dp(k, length-1)
                s += dpa
                # print(k,dpa,s)
                dp[k] =
            m[(start,length)] = s
            return s
        res = 0
        for k in [0,1,2,3,4,6,7,8,9]:
            res += dp(k,N) % (10**9+7)

        return res + (N == 1) * 1

test = True
if test:
    sol = Solution()
    case = [False]*2 + [True] + [False]*3
    if case[0]:
        # Example 1:
        Input = 1
        # Output: 10
        print(sol.knightDialer(Input))
    if case[1]:
        # Example 2:
        Input = 2
        # Output: 20
        print(sol.knightDialer(Input))
    if case[2]:
        # Example 3:
        Input = 3
        # Output: 46
        print(sol.knightDialer(Input))
