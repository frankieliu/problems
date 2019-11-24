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
        self.w = w
        self.d = defaultdict(list)
        for i, aw in enumerate(w):
            self.d[aw].append(i)
        print(self.d)
        self.dm = defaultdict(lambda: -1)

    def shortest(self, w1, w2):
        if (w1 == w2):
            return 0
        if (w2 < w1):
            w1, w2 = w2, w1
        if self.dm[(w1, w2)] == -1:
            amin = len(self.w)+1
            for a in self.d[w1]:
                for b in self.d[w2]:
                    amin = min(amin, abs(a-b))
            self.dm[(w1, w2)] = amin
        return self.dm[(w1, w2)]


test = True
if test:
    words = ["practice", "makes", "perfect", "coding", "makes"]
    e1 = ["coding", "practice"]
    e2 = ["makes", "coding"]

    # Your WordDistance object will be instantiated and called as such:
    obj = WordDistance(words)
    print(obj.shortest(*e1))
    print(obj.shortest(*e2))
