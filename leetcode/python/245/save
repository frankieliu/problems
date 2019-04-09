#
# @lc app=leetcode id=245 lang=python3
#
# [245] Shortest Word Distance III
#
# https://leetcode.com/problems/shortest-word-distance-iii/description/
#
# algorithms
# Medium (52.84%)
# Total Accepted:    36.3K
# Total Submissions: 68.7K
# Testcase Example:  '["practice", "makes", "perfect", "coding", "makes"]\n"makes"\n"coding"'
#
# Given a list of words and two words word1 and word2, return the shortest
# distance between these two words in the list.
#
# word1 and word2 may be the same and they represent two individual words in
# the list.
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Input: word1 = “makes”, word2 = “coding”
# Output: 1
#
#
#
# Input: word1 = "makes", word2 = "makes"
# Output: 3
#
#
# Note:
# You may assume word1 and word2 are both in the list.
#
#
class Solution:
    def shortestWordDistance(self, words, w1, w2):

        def same(words, w1):
            prev = -len(words)
            out = len(words) + 1
            for i in range(len(words)):
                if words[i] == w1:
                    out = min(out, i-prev)
                    prev = i
            return out

        if w1 == w2:
            return same(words, w1)

        out = len(words) + 1
        i1 = out
        i2 = -out
        for i in range(len(words)):
            if words[i] == w1:
                i1 = i
            elif words[i] == w2:
                i2 = i
            out = min(out, abs(i1 - i2))
        return out


test = True
if test:
    Example = ["practice", "makes", "perfect", "coding", "makes"]
    w1 = "makes"
    w2 = "coding"
    Example = ["a", "a"]
    w1 = "a"
    w2 = "a"
    s = Solution()
    print(s.shortestWordDistance(Example, w1, w2))
