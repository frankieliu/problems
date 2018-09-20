#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "implement-strStr.hpp"

/*
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1
if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

Clarification:

What should we return when needle is an empty string? This is a great
question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an
empty string. This is consistent to C's strstr() and Java's indexOf().
*/

TEST(Leetcode, implement_strStr_28) {
    Solution s;
    string haystack;
    string needle;

    haystack = "hello";
    needle = "ll";
    // EXPECT_EQ(2, s.strStr(haystack,needle));

    haystack = "aaaaa";
    needle = "bba";
    // EXPECT_EQ(-1, s.strStr(haystack,needle));

    haystack = "bbbbababbbaabbba";
    needle = "abb";
    // EXPECT_EQ(6, s.strStr(haystack,needle));

    haystack = "bbbbababbbaabbba";
    needle = "";
    EXPECT_EQ(0, s.strStr(haystack,needle));

}

