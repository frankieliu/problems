#
# @lc app=leetcode id=277 lang=python
#
# [277] Find the Celebrity
#
# https://leetcode.com/problems/find-the-celebrity/description/
#
# algorithms
# Medium (35.81%)
# Total Accepted:    76.8K
# Total Submissions: 214.4K
# Testcase Example:  '[[1,1,0],[0,1,0],[1,1,1]]'
#
# Suppose you are at a party with n people (labeled from 0 to n - 1) and among
# them, there may exist one celebrity. The definition of a celebrity is that
# all the other n - 1 people know him/her but he/she does not know any of
# them.
#
# Now you want to find out who the celebrity is or verify that there is not
# one. The only thing you are allowed to do is to ask questions like: "Hi, A.
# Do you know B?" to get information of whether A knows B. You need to find out
# the celebrity (or verify there is not one) by asking as few questions as
# possible (in the asymptotic sense).
#
# You are given a helper function bool knows(a, b) which tells you whether A
# knows B. Implement a function int findCelebrity(n). There will be exactly one
# celebrity if he/she is in the party. Return the celebrity's label if there is
# a celebrity in the party. If there is no celebrity, return -1.
#
#
#
# Example 1:
#
#
# Input: graph = [
# [1,1,0],
# [0,1,0],
# [1,1,1]
# ]
# Output: 1
# Explanation: There are three persons labeled with 0, 1 and 2. graph[i][j] = 1
# means person i knows person j, otherwise graph[i][j] = 0 means person i does
# not know person j. The celebrity is the person labeled as 1 because both 0
# and 2 know him but 1 does not know anybody.
#
#
# Example 2:
#
#
# Input: graph = [
# [1,0,1],
# [1,1,0],
# [0,1,1]
# ]
# Output: -1
# Explanation: There is no celebrity.
#
#
#
#
# Note:
#
#
# The directed graph is represented as an adjacency matrix, which is an n x n
# matrix where a[i][j] = 1 means person i knows person j while a[i][j] = 0
# means the contrary.
# Remember that you won't have direct access to the adjacency matrix.
#
#
#
# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find columns that add up to len(n)
        if len(n) <= 1:
            return -1

        csum = [0] * len(n[0])
        rsum = [0] * len(n)
        for j, row in enumerate(n):
            for i, col in enumerate(row):
                csum[i] += col
                rsum[j] += col
        for i, col in enumerate(csum):
            if col == len(n):
                if rsum[i] == 1:
                    return i
        return -1


test = True
if test:
    s = Solution()
    case = [True, False]
    if case[0]:
        graph = [
            [1, 0, 1],
            [0, 1, 1],
            [0, 0, 1]
        ]
        # Output: -1
        print(s.findCelebrity(graph))
    if case[1]:
        print(s.findCelebrity())