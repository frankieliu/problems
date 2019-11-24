#
# @lc app=leetcode id=743 lang=python3
#
# [743] Network Delay Time
#
# https://leetcode.com/problems/network-delay-time/description/
#
# algorithms
# Easy (39.37%)
# Total Accepted:    23K
# Total Submissions: 58.5K
# Testcase Example:  '[[2,1,1],[2,3,1],[3,4,1]]\n4\n2'
#
# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes
# for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all
# nodes to receive the signal? If it is impossible, return -1.
#
# Note:
#
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 1 <= w <=
# 100.
#
#
#
#
#
class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        d = [None] * N
        for i in range(0,N):
            d[i] = [6001] * N
        for u,v,w in times:
            d[u-1][v-1] = w
        for v in range(0,N):
            d[v][v] = 0
        for k in range(0,N):
            for i in range(0,N):
                for j in range(0,N):
                    if d[i][j] > d[i][k] + d[k][j]:
                        d[i][j] = d[i][k] + d[k][j]
        # print(d)
        m = 0
        for k in range(0,N):
            m = max(m, d[K-1][k])
            #print(d[K-1][k])
        if m == 6001:
            return -1
        else:
            return m

test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*0
    if case[0]:
        Example = [[2,1,1],[2,3,1],[3,4,1]]
        print(sol.networkDelayTime(Example,4,2))


