#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "plus-one.hpp"

/*
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single
digit.

You may assume the integer does not contain any leading zero, except
the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]

Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]

Explanation: The array represents the integer 4321.
*/

TEST(Leetcode, plus_one_66) {
    Solution s;
    vector<int> a={1,2,3};
    EXPECT_EQ(vector<int>({1,2,4}), s.plusOne(a));
    vector<int> b={9,9,9};
    EXPECT_EQ(vector<int>({1,0,0,0}), s.plusOne(b));
}
