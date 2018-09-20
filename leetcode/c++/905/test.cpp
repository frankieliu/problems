#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "sort-array-by-parity.hpp"

/*
Given an array A of non-negative integers, return an array consisting
of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

Example 1:
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Note:
1 <= A.length <= 5000
0 <= A[i] <= 5000
*/

TEST(Leetcode, sort_array_by_parity_905) {
    Solution s;
    vector<int> a={1,2,3,4,5,6,7};
    EXPECT_EQ((vector<int>{6,2,4,5,3,7,1}),
              s.sortArrayByParity(a));
    vector<int> b={};
    EXPECT_EQ(b, s.sortArrayByParity(b));
}
