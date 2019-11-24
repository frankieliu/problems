# 8638970544 121042882
# @lc app=leetcode id=887 lang=python3
#
# [887] Super Egg Drop
#
# https://leetcode.com/problems/super-egg-drop/description/
#
# algorithms
# Hard (24.35%)
# Total Accepted:    5K
# Total Submissions: 20.4K
# Testcase Example:  '1\n2'
#
# You are given K eggs, and you have access to a building with N floors from 1
# to N. 
#
# Each egg is identical in function, and if an egg breaks, you cannot drop it
# again.
#
# You know that there exists a floor F with 0 <= F <= N such that any egg
# dropped at a floor higher than F will break, and any egg dropped at or below
# floor F will not break.
#
# Each move, you may take an egg (if you have an unbroken one) and drop it from
# any floor X (with 1 <= X <= N). 
#
# Your goal is to know with certainty what the value of F is.
#
# What is the minimum number of moves that you need to know with certainty what
# F is, regardless of the initial value of F?
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
# Input: K = 1, N = 2
# Output: 2
# Explanation:
# Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
# Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty
# that F = 1.
# If it didn't break, then we know with certainty F = 2.
# Hence, we needed 2 moves in the worst case to know what F is with
# certainty.
#
#
#
# Example 2:
#
#
# Input: K = 2, N = 6
# Output: 3
#
#
#
# Example 3:
#
#
# Input: K = 3, N = 14
# Output: 4
#
#
#
#
# Note:
#
#
# 1 <= K <= 100
# 1 <= N <= 10000
#
#
#
#
#
#
class Solution:
    def superEggDrop(self, K, N):
        """
        K number of eggs
        N number of floors
        return min number of moves required
        """
        """
        dp[k][n] : least number of moves required for
                   k eggs and n floors
        dp[k][n] = dp[k][n/2]   - if it didn't break at n/2 floor
                   dp[k-1][n/2] - if it did break

        so we can the max of both of these cases, one in which it did
        break and one in which it did not break, we take the max because
        that is the worst case

        In general may want to figure out which floor to drop it from
        say some floor m, then

        dp[k][n] = min_m max(dp[k][n-m] + dp[k-1][m-1])

        - the number of moves required is monotonic with n, so we
          need to find a crossing between dp[k][n-m] and dp[k-1][m-1]
          with a binary search

        T1 = dp(K-1,X-1) corresponds to breaking @ X
        T2 = dp(K, N-X)  corresponds to not breaking @ X

        T1 is an increasing sequence
        T2 is a decreasing sequence

        if T1 > T2 then move left: (intersection in left)
          hi = x

        if T1 < T2 then move right: (intersection in right)
          lo = x

        else:
          lo = hi = x




        """



test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*3
    if case[0]:
        # Example 1:
        K = 1
        N = 2
        # Output: 2
        print(sol.superEggDrop(K, N))
    if case[1]:
        # Example 2:
        K = 2
        N = 6
        # Output: 3
        print(sol.superEggDrop(K, N))
    if case[2]:
        # Example 3:
        K = 3
        N = 14
        # Output: 4
        print(sol.superEggDrop(K, N))
