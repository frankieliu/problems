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

        # left right mirrors
        mirr = [["0", "0"], ["1", "1"], ["8", "8"], ["6", "9"], ["9", "6"]]
        # for 180 mirrors
        mid = ["0", "1", "8"]

        mirr_hash = dict(mirr)
        k = list(mirr_hash.keys())
        c = product(k, repeat=n//2)
        d = [list(x) for x in c]
        if n > 1:
            e = [list(x) for x in d if x[0] != "0"]
        else:
            e = [list(x) for x in d]
        # print("list e", list(e))
        # print("prod", list(product(c, mid)))

        # adds a mid element if odd
        if n % 2 == 1:
            f = [list(chain(*x)) for x in product(e, mid)]
        else:
            f = e

        # add palidrome
        for x in f:
            x.extend([mirr_hash[y] for y in reversed(x[0:(n//2)])])
        return ["".join(x) for x in f]


test = True
if test:
    s = Solution()
    print(list(s.findStrobogrammatic(4)))
