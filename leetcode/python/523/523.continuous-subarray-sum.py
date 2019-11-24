#
# @lc app=leetcode id=523 lang=python3
#
# [523] Continuous Subarray Sum
#
# https://leetcode.com/problems/continuous-subarray-sum/description/
#
# algorithms
# Medium (24.04%)
# Total Accepted:    55.8K
# Total Submissions: 232.1K
# Testcase Example:  '[23,2,4,6,7]\n6'
#
#
# Given a list of non-negative numbers and a target integer k, write a function
# to check if the array has a continuous subarray of size at least 2 that sums
# up to the multiple of k, that is, sums up to n*k where n is also an
# integer.
#
#
#
# Example 1:
#
# Input: [23, 2, 4, 6, 7],  k=6
# Output: True
# Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to
# 6.
#
#
#
#
# Example 2:
#
# Input: [23, 2, 6, 4, 7],  k=6
# Output: True
# Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and
# sums up to 42.
#
#
#
# Note:
#
# The length of the array won't exceed 10,000.
# You may assume the sum of all the numbers is in the range of a signed 32-bit
# integer.
#
#
#
class Solution:
    def checkSubarraySum(self, n, k):
        if len(n) < 2:
            return False

        if sum(n) == 0:
            return True

        if k == 0 and sum(n) != 0:
            return False

        k = abs(k)
        m = set()
        for i, el in enumerate(n):
            if i != 0:
                if len(m) == 0:
                    m.add(el)
                else:
                    print(m, el, [(x + el) % k for x in m])
                    m.add([(x + el) % k for x in m])
            if i == 0 and el % k != 0:
                m.add(el % k)
            if 0 in m and n[0] % k != 0:
                return True
        return False


test = True
if test:
    sol = Solution()
    case = [False]*0 + [True] + [False]*2
    if case[0]:
        # Example 1:
        Input = [23,2,4,6,7]
        k = 2
        # Output: True
        print(sol.checkSubarraySum(Input, k))
    if case[1]:
        # Example 2:
        k = 6
        # Output: True
        print(sol.checkSubarraySum(k))
