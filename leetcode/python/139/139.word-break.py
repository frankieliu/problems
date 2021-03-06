#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.com/problems/word-break/description/
#
# algorithms
# Medium (33.97%)
# Total Accepted:    292.1K
# Total Submissions: 859.6K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a non-empty string s and a dictionary wordDict containing a list of
# non-empty words, determine if s can be segmented into a space-separated
# sequence of one or more dictionary words.
#
# Note:
#
#
# The same word in the dictionary may be reused multiple times in the
# segmentation.
# You may assume the dictionary does not contain duplicate words.
#
#
# Example 1:
#
#
# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
#
#
# Example 2:
#
#
# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
#
#
# Example 3:
#
#
# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false
#
#
#
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        dp = [False]*(len(s)+1)
        # solving for dp[i]

        # empty string
        dp[len(s)] = True
        for i in range(len(s)-1, -1, -1):
            sol = False
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    sol = sol or dp[j]
            dp[i] = sol
        # print(dp)
        return dp[0]


test = False
if test:
    s = Solution()
    st = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(s.wordBreak(st, wordDict))

    st = "applepenapple"
    wordDict = ["apple", "pen"]
    print(s.wordBreak(st, wordDict))
