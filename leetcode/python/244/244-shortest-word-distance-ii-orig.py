#
# @lc app=leetcode id=244 lang=python3
#
# [244] Shortest Word Distance II
#
# https://leetcode.com/problems/shortest-word-distance-ii/description/
#
# algorithms
# Medium (46.29%)
# Total Accepted:    44.6K
# Total Submissions: 96.3K
# Testcase Example:  '["WordDistance","shortest","shortest"]\n[[["practice","makes","perfect","coding","makes"]],["coding","practice"],["makes","coding"]]'
#
# Design a class which receives a list of words in the constructor, and
# implements a method that takes two words word1 and word2 and return the
# shortest distance between these two words in the list. Your method will be
# called repeatedly many times with different parameters. 
#
# Example:
# Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
#
#
# Input: word1 = “coding”, word2 = “practice”
# Output: 3
#
#
from collections import defaultdict

class WordDistance:
    def __init__(self, w):
        self.h = defaultdict(list)
        for i, el in enumerate(w):
            self.h[el].append(i)
        self.max = len(w)

    def shortest(self, w1, w2):
        l1 = self.h[w1]
        l2 = self.h[w2]
        i, j = 0, 0
        out = self.max
        while i < len(l1) and j < len(l2):
            out = min(out, abs(l1[i] - l2[j]))
            if out == 0:
                break
            if l1[i] > l2[j]:
                j += 1
            else:
                i += 1
        return out


test = True
if test:
    words = ["practice", "makes", "perfect", "coding", "makes"]
    e1 = ["coding", "practice"]
    e2 = ["makes", "coding"]

    # Your WordDistance object will be instantiated and called as such:
    obj = WordDistance(words)
    print(obj.shortest(*e1))
    print(obj.shortest(*e2))
