#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "sum-of-subarray-minimums.hpp"

/*

Given an array of integers A, find the sum of min(B), where B ranges
over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.

Example 1:

Input: [3,1,2,4]
Output: 17

Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4],
[3,1,2], [1,2,4], [3,1,2,4].

Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.

Note:

1 <= A.length <= 30000
1 <= A[i] <= 30000

*/

TEST(Leetcode, sum_of_subarray_minimums_907) {
    Solution s;
    // vector<int> a={3,1,2,4};
    // EXPECT_EQ(17, s.sumSubarrayMins(a));
    if(false){
        vector<int> a={};
        EXPECT_EQ(0, s.sumSubarrayMins(a));
        vector<int> b={1};
        EXPECT_EQ(1, s.sumSubarrayMins(b));
        vector<int> c={1,2};
        EXPECT_EQ(1+2+1, s.sumSubarrayMins(c));
        EXPECT_EQ(vector<int>({1,2,1,1}),
                  s.leetLeft(vector<int>({3,1,2,4})));
        EXPECT_EQ(vector<int>({1,3,2,1}),
                  s.leetRight(vector<int>({3,1,2,4})));
    }
    vector<int> a({3,1,2,4});
    EXPECT_EQ(17, s.sumSubarrayMins(a));
}


