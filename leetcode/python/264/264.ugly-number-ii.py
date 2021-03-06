#
# @lc app=leetcode id=264 lang=python3
#
# [264] Ugly Number II
#
# https://leetcode.com/problems/ugly-number-ii/description/
#
# algorithms
# Medium (35.32%)
# Total Accepted:    94.9K
# Total Submissions: 268.6K
# Testcase Example:  '10'
#
# Write a program to find the n-th ugly number.
#
# Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
#
# Example:
#
#
# Input: n = 10
# Output: 12
# Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10
# ugly numbers.
#
# Note:  
#
#
# 1 is typically treated as an ugly number.
# n does not exceed 1690.
#
#
class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        '''
        keep track of the last
        smallest that got multiplied
        '''
        if n == 1:
            return 1
        a = [0] * n
        n -= 1
        idx = 0
        a[0] = 1
        idx = 1
        n2, n3, n5 = 0, 0, 0
        while True:
            m = min(a[n2]*2, a[n3]*3, a[n5]*5)
            a[idx] = m
            if m == a[n2]*2:
                n2 += 1
            if m == a[n3]*3:
                n3 += 1
            if m == a[n5]*5:
                n5 += 1
            if idx == n:
                return a[idx]
            idx += 1


test = True
if test:
    s = Solution()
    for i in range(1,11):
        print(s.nthUglyNumber(i))
