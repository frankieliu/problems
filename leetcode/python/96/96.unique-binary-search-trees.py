#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#
# https://leetcode.com/problems/unique-binary-search-trees/description/
#
# algorithms
# Medium (44.68%)
# Total Accepted:    180.8K
# Total Submissions: 404.6K
# Testcase Example:  '3'
#
# Given n, how many structurally unique BST's (binary search trees) that store
# values 1 ... n?
#
# Example:
#
#
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#
# ⁠  1         3     3      2      1
# ⁠   \       /     /      / \      \
# ⁠    3     2     1      1   3      2
# ⁠   /     /       \                 \
# ⁠  2     1         2                 3
#
#
#
class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 1:
            return 1

        if n == 2:
            return 2

        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        for j in range(3, n+1):
            out = 0
            for i in range(1, j+1):
                nl = i-1
                nr = j-i
                out += dp[nl] * dp[nr]
            dp[j] = out
        return dp[n]


test = True
if test:
    s = Solution()
    print(s.numTrees(3))
