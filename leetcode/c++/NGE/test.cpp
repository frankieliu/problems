#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "next-greater-element.hpp"

/*
*/

TEST(Leetcode, next_greater_element_1) {
    Solution s;
    vector<int> a={3,1,4,5};
    EXPECT_EQ(vector<int>({4,4,5,-1}), s.nge(a));
    // vector<int> b={,};
    // EXPECT_EQ(, s.(b));
}
