#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#
# https://leetcode.com/problems/interleaving-string/description/
#
# algorithms
# Hard (27.03%)
# Total Accepted:    101.9K
# Total Submissions: 377.1K
# Testcase Example:  '"aabcc"\n"dbbca"\n"aadbbcbcac"'
#
# Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and
# s2.
#
# Example 1:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# Output: true
#
#
# Example 2:
#
#
# Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# Output: false
#
#
#
class Solution:
    """ From @caikehe """

    def isInterleave1(self, s1, s2, s3):
        r, c, ll = len(s1), len(s2), len(s3)
        if r + c != ll:
            return False
        dp = [None] * (r + 1)
        for i in range(len(dp)):
            dp[i] = [None] * (c + 1)

        dp[-1][-1] = True

        # we use the indexing trick in python -1 is the last element
        # wrap around
        # Use the -1 index to indicate no string being consumed so far
        for i in range(0, r):
            dp[i][-1] = dp[i - 1][-1] and s1[i] == s3[i]

        for j in range(0, c):
            dp[-1][j] = dp[-1][j - 1] and s2[j] == s3[j]

        for i in range(0, r):
            for j in range(0, c):
                dp[i][j] = ((dp[i - 1][j] and s1[i] == s3[i + j + 1])
                            or (dp[i][j - 1] and s2[j] == s3[i + j + 1]))

        return dp[r - 1][c - 1]

    def isInterleave2(self, s1, s2, s3):
        """ O(n) space """

        r, c, ll = len(s1), len(s2), len(s3)
        if r + c != ll:
            return False
        dp = [None] * (c + 1)  # single row
        dp[-1] = True

        for j in range(0, c):
            dp[j] = dp[j - 1] and s2[j] == s3[j]

        for i in range(0, r):
            dp[-1] = (dp[-1] and s1[i] == s3[i])
            for j in range(0, c):
                dp[j] = ((dp[j] and s1[i] == s3[i + j + 1])
                         or (dp[j - 1] and s2[j] == s3[i + j + 1]))

        return dp[c - 1]

    def isInterleave3(self, s1, s2, s3):
        """ DFS """
        r, c, ll = len(s1), len(s2), len(s3)
        if r + c != ll:
            return False
        s, v = [(0, 0)], set((0, 0))
        while s:
            x, y = s.pop()
            if x + y == ll:
                return True
            nnext = (x+1, y)
            if (x+1 <= r and nnext not in v and s1[x] == s3[x + y]):
                s.append(nnext)
                v.add(nnext)
            nnext = (x, y+1)
            if (y+1 <= c and nnext not in v and s2[y] == s3[x + y]):
                s.append(nnext)
                v.add(nnext)
        return False

    def isInterleave(self, s1, s2, s3):
        """ BFS """
        r, c, ll = len(s1), len(s2), len(s3)
        if r + c != ll:
            return False
        s, v = [(0, 0)], set((0, 0))
        while s:
            x, y = s.pop(0)
            if x + y == ll:
                return True
            nnext = (x+1, y)
            if (x+1 <= r and nnext not in v and s1[x] == s3[x + y]):
                s.append(nnext)
                v.add(nnext)
            nnext = (x, y+1)
            if (y+1 <= c and nnext not in v and s2[y] == s3[x + y]):
                s.append(nnext)
                v.add(nnext)
        return False


test = True
if test:
    sol = Solution()
    case = [False] * 0 + [True] + [False] * 2
    if case[0]:
        # Example 1:
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbcbcac"
        # Output: true
        print(sol.isInterleave(s1, s2, s3))
    if case[1]:
        # Example 2:
        s1 = "aabcc"
        s2 = "dbbca"
        s3 = "aadbbbaccc"
        # Output: false
        print(sol.isInterleave(s1, s2, s3))
