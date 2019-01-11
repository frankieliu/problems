"""69. Sqrt(x)
Easy

600

1109

Favorite

Share
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
Accepted
306,806
Submissions
1,018,382"""

class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0:
            return 0

        # newton's method
        x0 = x/2 # initial guess
        prev = x

        while True:
            # x0 = x0 - (x0^2-3)/(2*x0)
            # print(x0)
            x0 = 0.5*(x0 + x/x0)
            if abs(prev - x0) < 0.1:
                return int(x0)
            prev = x0
