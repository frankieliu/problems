"""29. Divide Two Integers
Medium

521

2476

Favorite

Share

Given two integers dividend and divisor, divide two integers without
using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

Both dividend and divisor will be 32-bit signed integers.

The divisor will never be 0.

Assume we are dealing with an environment which could only store
integers within the 32-bit signed integer range: [−231, 231 − 1]. For
the purpose of this problem, assume that your function returns 231 − 1
when the division result overflows.

Accepted
169.7K
Submissions
1.1M

"""
class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        sign = 1
        if dividend < 0:
            sign = -sign
            dividend = -dividend
        if divisor < 0:
            sign = -sign
            divisor = -divisor

        ans = 0
        while dividend >= divisor:
            n = 0
            while (divisor << n) <= dividend:
                n += 1
            ans += 1 << (n-1)
            dividend -= (divisor << (n-1))

        if sign == 1:
            return min((1<<31) - 1, ans)
        else:
            return max(-(1<<31), -ans)

s = Solution()
print(s.divide(7, -3))
