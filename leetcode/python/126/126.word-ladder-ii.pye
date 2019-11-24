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
from typing import List
import collections

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        tree, wordSet, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordSet:
            return []

        found, fq, bq, nq, isForward = False, {beginWord}, {endWord}, set(), True
        while fq and not found:
            wordSet -= fq
            for curWord in fq:
                for i in range(len(curWord)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        nextWord = curWord[:i] + c + curWord[i + 1:]
                        if nextWord in wordSet:
                            if nextWord in bq:
                                found = True
                            else:
                                nq.add(nextWord)
                            tree[curWord].add(nextWord) if isForward else tree[nextWord].add(curWord)
            fq.clear()
            fq, nq = nq, fq
            if len(fq) > len(bq):
                fq, bq, isForward = bq, fq, not isForward

        def bt(word):
            if word == endWord:
                return [[word]]

            res = []
            for nextWord in tree[word]:
                results = bt(nextWord)
                for result in results:
                    result.insert(0, word)
                    res.append(result)

            return res
        return bt(beginWord)
