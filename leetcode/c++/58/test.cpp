#include <gtest/gtest.h>
#include "../base/cpp_standards.h"
#include "length-of-last-word.hpp"

/*
Given a string s consists of upper/lower-case alphabets and empty
space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space
characters only.

Example:
Input: "Hello World"
Output: 5
*/

TEST(Leetcode, length_of_last_word_58) {
    Solution s;
    EXPECT_EQ(5, s.lengthOfLastWord("Hello world"));
    EXPECT_EQ(0, s.lengthOfLastWord(""));
    EXPECT_EQ(1, s.lengthOfLastWord("a"));
    EXPECT_EQ(1, s.lengthOfLastWord("a "));
}
