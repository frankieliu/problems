#
# @lc app=leetcode id=247 lang=python3
#
# [247] Strobogrammatic Number II
#
# https://leetcode.com/problems/strobogrammatic-number-ii/description/
#
# algorithms
# Medium (43.72%)
# Total Accepted:    44.5K
# Total Submissions: 101.8K
# Testcase Example:  '2'
#
# A strobogrammatic number is a number that looks the same when rotated 180
# degrees (looked at upside down).
#
# Find all strobogrammatic numbers that are of length = n.
#
# Example:
#
#
# Input:  n = 2
# Output: ["11","69","88","96"]
#
#
#
from itertools import permutations, product, chain


class Solution:
    def findStrobogrammatic(self, n):
        if n == 1:
            return ["0","1","8"]
        # numbers that are strobe
        # length 1
        # 1691
        m = {
            0: 0,
            1: 1,
            6: 9,
            9: 6,
            8:8}
        a = 0
        a = list(product([0,1,6,9,8], repeat=(n+1)//2))

        def map9(x):
            if x == 6:
                return 9
            if x == 9:
                return 6
            return x

        def nonzero(x):
            sx = "".join(map(str,x))
            return str(int(sx)) == sx and int(sx) != 0

        if n & 1 == 1:
            b = [list(x) for x in a if nonzero(x) and x[-1] not in [6,9]]
            c = [x + list(map(map9,reversed(x[0:-1]))) for x in b]
        else:
            b = [list(x) for x in a if nonzero(x)]
            c = [x + list(map(map9,x[::-1])) for x in b]


        return sorted(["".join(map(str,x)) for x in c])
test = True
if test:
    s = Solution()
    print(s.findStrobogrammatic(2))
