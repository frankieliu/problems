#
# @lc app=leetcode id=989 lang=python3
#
# [989] Add to Array-Form of Integer
#
# https://leetcode.com/problems/add-to-array-form-of-integer/description/
#
# algorithms
# Easy (44.93%)
# Total Accepted:    9.2K
# Total Submissions: 20.4K
# Testcase Example:  '[1,2,0,0]\n34'
#
# For a non-negative integer X, the array-form of X is an array of its digits
# in left to right order.  For example, if X = 1231, then the array form is
# [1,2,3,1].
#
# Given the array-form A of a non-negative integer X, return the array-form of
# the integer X+K.
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
# Input: A = [1,2,0,0], K = 34
# Output: [1,2,3,4]
# Explanation: 1200 + 34 = 1234
#
#
#
# Example 2:
#
#
# Input: A = [2,7,4], K = 181
# Output: [4,5,5]
# Explanation: 274 + 181 = 455
#
#
#
# Example 3:
#
#
# Input: A = [2,1,5], K = 806
# Output: [1,0,2,1]
# Explanation: 215 + 806 = 1021
#
#
#
# Example 4:
#
#
# Input: A = [9,9,9,9,9,9,9,9,9,9], K = 1
# Output: [1,0,0,0,0,0,0,0,0,0,0]
# Explanation: 9999999999 + 1 = 10000000000
#
#
#
#
# Note：
#
#
# 1 <= A.length <= 10000
# 0 <= A[i] <= 9
# 0 <= K <= 10000
# If A.length > 1, then A[0] != 0
#
#
#
#
#
#
from typing import *


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:

        if A is None:
            return 0

        out = []
        c = 0
        for el in reversed(A):
            r = K % 10
            K = K // 10
            s = r + el + c
            c = s // 10
            print(r, K, s, c)
            out.append(s % 10)

        print(K, c, out)
        if (c + K) > 0:
            s = c + K
            while s > 0:
                out.append(s % 10)
                s = s // 10

        return list(reversed(out))


test = True
if test:
    s = Solution()
    case = [False] * 0 + [True] + [False] * 4
    if case[0]:
        A = [1, 2, 0, 0]
        K = 34
        A = [0]
        K = 10000
        print(s.addToArrayForm(A, K))
    if case[1]:
        A = [2, 7, 4]
        K = 181
        print(s.addToArrayForm(A, K))
    if case[2]:
        A = [2, 1, 5]
        K = 806
        print(s.addToArrayForm(A, K))
    if case[3]:
        A = [9, 9, 9, 9, 9, 9, 9, 9, 9, 9]
        K = 1
        print(s.addToArrayForm(A, K))
