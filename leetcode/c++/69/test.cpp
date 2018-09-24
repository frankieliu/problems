#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "sqrt.hpp"

/*
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a
non-negative integer.

Since the return type is an integer, the decimal digits are truncated
and only the integer part of the result is returned.

Example 1:
Input: 4
Output: 2

Example 2:
Input: 8
Output: 2

Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

Using newton's method: 
   . y0
  .
..
   x0

rt = x^2
y = x^2 - rt 

x1 = x0 - y0/slope(@x0)
   = x0 - (x0^2 - rt) / 2 x0
   = x0 - 0.5 * x0 + 0.5 rt/x0
   = 0.5 (x0 + rt/x0)

*/

TEST(Leetcode, sqrt_69) {
    Solution s;
    EXPECT_EQ(2, s.mySqrt(4));
    EXPECT_EQ(46339, s.mySqrt(2147395599));
}
