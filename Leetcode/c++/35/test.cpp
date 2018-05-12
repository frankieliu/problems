#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "search-insert-position.hpp"

/*
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
*/

TEST(Leetcode, search_insert_position_35) {
    Solution s;
    vector<int> a={,};
    EXPECT_EQ(, s.(a));
    vector<int> b={,};
    EXPECT_EQ(, s.(b));
}
