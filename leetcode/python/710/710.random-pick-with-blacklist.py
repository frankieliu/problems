#
# @lc app=leetcode id=710 lang=python3
#
# [710] Random Pick with Blacklist
#
# https://leetcode.com/problems/random-pick-with-blacklist/description/
#
# algorithms
# Hard (30.58%)
# Total Accepted:    4.1K
# Total Submissions: 13.4K
# Testcase Example:  '["Solution", "pick", "pick", "pick"]\n[[1, []], [], [], []]'
#
# Given a blacklist B containing unique integers from [0, N), write a function
# to return a uniform random integer from [0, N) which is NOT in B.
#
# Optimize it such that it minimizes the call to system’s Math.random().
#
# Note:
#
#
# 1 <= N <= 1000000000
# 0 <= B.length < min(100000, N)
# [0, N) does NOT include N. See interval notation.
#
#
# Example 1:
#
#
# Input:
# ["Solution","pick","pick","pick"]
# [[1,[]],[],[],[]]
# Output: [null,0,0,0]
#
#
# Example 2:
#
#
# Input:
# ["Solution","pick","pick","pick"]
# [[2,[]],[],[],[]]
# Output: [null,1,1,1]
#
#
# Example 3:
#
#
# Input:
# ["Solution","pick","pick","pick"]
# [[3,[1]],[],[],[]]
# Output: [null,0,0,2]
#
#
# Example 4:
#
#
# Input:
# ["Solution","pick","pick","pick"]
# [[4,[2]],[],[],[]]
# Output: [null,1,3,1]
#
#
# Explanation of Input Syntax:
#
# The input is two lists: the subroutines called and their arguments.
# Solution's constructor has two arguments, N and the blacklist B. pick has no
# arguments. Arguments are always wrapped with a list, even if there aren't
# any.
#
#
from random import randint
class Solution:

    def __init__(self, N, blacklist):
        """
        0 .. N-1  : original range
        blen = length of blacklist

        Idea:
        map elements in the blacklist ([bl,..]) to some good number

        Divide: the original range into 0..N-1 into two parts

        0..N-blen-1   N-blen..N-1

        if a bl falls in N-blen..N-1, then we don't do anything because
        we will be picking from 0..N-blen-1 anyway

        if a bl falls in 0..N-blen-1, then we need to map to some available
        number in N-beln..N-1 range that is not in the blacklist
        """
        self.N = N
        blen = len(blacklist)
        self.blen = blen
        m = {}
        i = N-blen    # where we begin search for a good number
        bl = set(blacklist)
        for b in blacklist:
            if b >= N-blen:  # already in sectioned off area
                continue
            # find a "good" mapping in the sectioned off area
            while i in bl:
                i += 1
            m[b] = i
            i += 1
        self.m = m

    def pick(self):
        k = randint(0, self.N - self.blen - 1)
        if k in self.m:
            return self.m[k]
        else:
            return k


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
test = True
if test:
    sol = Solution(12, [1, 3])
    for i in range(0, 10):
        print(sol.pick())
