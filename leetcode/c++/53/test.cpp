#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "maximum-subarray.hpp"

/*
Given an integer array nums, find the contiguous subarray (containing
at least one number) which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution
using the divide and conquer approach, which is more subtle.
*/

// consider all subarrays ending in a[i]
// [-2, 1, -3, 4, -1, 2, 1, -5, 4]
// [-2]
// [-2 1] [1]
// [-2 1 -3] [1 -3] [-3]
// [-2 1 -3 4] [1 -3 4] [-3 4] [4]
//
// We note that the subarrays increase by one each time
// And that we can discover the next of maximums by considering
// the max of ((max[i-1] + a[i]), a[i])

TEST(Leetcode, maximum_subarray_53) {
    Solution s;
    vector<int> a={-2,1,-3,4,-1,2,1,-5,4};
    EXPECT_EQ(6, s.maxSubArray(a));
}
