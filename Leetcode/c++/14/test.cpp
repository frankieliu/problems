#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "longest-common-prefix.hpp"

/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
*/

TEST(Leetcode, longest_common_prefix_14) {
    Solution s;
    vector<int> a={,};
    EXPECT_EQ(, s.(a));
    vector<int> b={,};
    EXPECT_EQ(, s.(b));
}
