#
# @lc app=leetcode id=564 lang=python3
#
# [564] Find the Closest Palindrome
#
# https://leetcode.com/problems/find-the-closest-palindrome/description/
#
# algorithms
# Hard (17.97%)
# Total Accepted:    11.1K
# Total Submissions: 61.9K
# Testcase Example:  '"1"'
#
# Given an integer n, find the closest integer (not including itself), which is
# a palindrome.
#
# The 'closest' is defined as absolute difference minimized between two
# integers.
#
# Example 1:
#
# Input: "123"
# Output: "121"
#
#
#
# Note:
#
# The input n is a positive integer represented by string, whose length will
# not exceed 18.
# If there is a tie, return the smaller one as answer.
#
#
#
class Solution:
    def nearestPalindromic(self, n):
        sn2 = n[0:(len(n)+1)//2]
        mind = 100**len(n)
        res = 0
        for x in range(-1, 2):
            sn3 = str(int(sn2)+x)
            lendiff = len(sn3) - len(sn2)
            if sn3 == "0" and len(n) > 1:
                candidate = "9"
            else:
                candidate = (
                    sn3 +
                    ((lendiff < 0) and
                     (len(n) % 2 == 0) and
                     "9" or "") +
                    sn3[0:(len(n) -
                           ((len(n) % 2 != 0) and lendiff or 0))//2][::-1])
            ndiff = abs(int(candidate) - int(n))
            print(candidate, n, ndiff)
            if ndiff < mind and ndiff > 0:
                mind = ndiff
                res = candidate
        return res

"""
 999
100
"""
test = True
if test:
    sol = Solution()
    case = [False]*2 + [True] + [False]*1
    if case[0]:
        # Example 1:
        Input = "123"
        # Output: "121"
        print(sol.nearestPalindromic(Input))
    if case[1]:
        # Example 1:
        Input = "1001"
        # Output: "121"
        print(sol.nearestPalindromic(Input))
    if case[2]:
        # Example 1:
        Input = "999"
        # Output: "121"
        print(sol.nearestPalindromic(Input))
