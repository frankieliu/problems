#include "67/leetcode_67.h"
#include "gtest/gtest.h"

TEST(AddBinaryTest, Test1) {
  Solution solution;
  string a = "0";
  EXPECT_STREQ(solution.addBinary("0", "0").c_str(), a.c_str());
  // EXPECT_STREQ("0", "0");
}

int main(int argc, char** argv) {
  ::testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
