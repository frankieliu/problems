#
# @lc app=leetcode id=354 lang=python3
#
# [354] Russian Doll Envelopes
#
# https://leetcode.com/problems/russian-doll-envelopes/description/
#
# algorithms
# Hard (33.39%)
# Total Accepted:    40K
# Total Submissions: 119.8K
# Testcase Example:  '[[5,4],[6,4],[6,7],[2,3]]'
#
# You have a number of envelopes with widths and heights given as a pair of
# integers (w, h). One envelope can fit into another if and only if both the
# width and height of one envelope is greater than the width and height of the
# other envelope.
#
# What is the maximum number of envelopes can you Russian doll? (put one inside
# other)
#
# Note:
# Rotation is not allowed.
#
# Example:
#
#
#
# Input: [[5,4],[6,4],[6,7],[2,3]]
# Output: 3
# Explanation: The maximum number of envelopes you can Russian doll is 3 ([2,3]
# => [5,4] => [6,7]).
#
#
#
#
import bisect

class Solution:
    def maxEnvelopes(self, envelopes):
        if len(envelopes) == 0 or len(envelopes[0]) != 2:
            return 0
        e = [(x,-y) for x,y in envelopes]
        print(sorted(e))
        e = [(x,y) for x,y in envelopes]
        dp = [0]*len(e)
        res = 0
        for el in e:
            i = bisect.bisect_left(dp, 0, el[1], res)
            if i < 0:
                i = -(i+1)
            dp[i] = el[1]
            if i == res:
                res+=1
        return res


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*1
    if case[0]:
        # Example:
        Input = [[5,4],[6,4],[6,7],[2,3]]
        # Output: 3
        print(sol.maxEnvelopes(Input))
