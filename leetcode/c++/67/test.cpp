#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "add-binary.hpp"

/*

Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or
0.

Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"
*/

TEST(Leetcode, add_binary_67) {
    Solution s;
    EXPECT_EQ("100", s.addBinary("11","1"));
    EXPECT_EQ("10101", s.addBinary("1010","1011"));
}
