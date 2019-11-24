#
# @lc app=leetcode id=126 lang=python3
#
# [126] Word Ladder II
#
# https://leetcode.com/problems/word-ladder-ii/description/
#
# algorithms
# Hard (16.71%)
# Total Accepted:    106.9K
# Total Submissions: 640.1K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# all shortest transformation sequence(s) from beginWord to endWord, such
# that:
#
#
# Only one letter can be changed at a time
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return an empty list if there is no such transformation sequence.
# All words have the same length.
# All words contain only lowercase alphabetic characters.
# You may assume no duplicates in the word list.
# You may assume beginWord and endWord are non-empty and are not the same.
#
#
# Example 1:
#
#
# Input:
# beginWord = "hit",
# endWord = "cog",
# wordList = ["hot","dot","dog","lot","log","cog"]
#
# Output:
# [
# ⁠ ["hit","hot","dot","dog","cog"],
# ["hit","hot","lot","log","cog"]
# ]
#
#
# Example 2:
#
#
# Input:
# beginWord = "hit"
# endWord = "cog"
# wordList = ["hot","dot","dog","lot","log"]
#
# Output: []
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        from collections import defaultdict
        fq, bq, isForw = set([beginWord]), set([endWord]), True
        done = False
        res = []

        tree = defaultdict(set)
        wordSet = set(wordList)

        if endWord not in wordSet:
            return res

        while not done and fq:

            l = len(fq)
            for w in fq:
                wordSet.discard(w)

            nq = set()
            for i in range(l):
                curWord = fq.pop()
                for j in range(len(curWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = curWord[:j] + c + curWord[j+1:]
                        if nextWord in wordSet:
                            if nextWord in bq:
                                done = True
                            else:
                                nq.add(nextWord)
                            tree[curWord].add(nextWord) if isForw else tree[nextWord].add(curWord)
            fq = nq
            if len(fq) > len(bq):
                fq, bq, isForw = bq, fq, not isForw

        self.dfs(beginWord, tree, endWord, [beginWord], res)
        return res

    def dfs(self, bw, tree, ew, path, res):
        if bw == ew:
            res.append(path[:])
            return

        for w in tree[bw]:
            path.append(w)
            self.dfs(w, tree, ew, path, res)
            path.pop()
