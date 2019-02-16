#
# @lc app=leetcode id=127 lang=python3
#
# [127] Word Ladder
#
# https://leetcode.com/problems/word-ladder/description/
#
# algorithms
# Medium (22.51%)
# Total Accepted:    223.2K
# Total Submissions: 991.4K
# Testcase Example:  '"hit"\n"cog"\n["hot","dot","dog","lot","log","cog"]'
#
# Given two words (beginWord and endWord), and a dictionary's word list, find
# the length of shortest transformation sequence from beginWord to endWord,
# such that:
#
#
# Only one letter can be changed at a time.
# Each transformed word must exist in the word list. Note that beginWord is not
# a transformed word.
#
#
# Note:
#
#
# Return 0 if there is no such transformation sequence.
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
# Output: 5
#
# Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" ->
# "dog" -> "cog",
# return its length 5.
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
# Output: 0
#
# Explanation: The endWord "cog" is not in wordList, therefore no possible
# transformation.
#
#
#
#
#
#
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return len([])
        if beginWord == endWord:
            return len([beginWord])

        # create a graph from wordList
        g = defaultdict(set)
        lwl = len(wordList)
        for i in range(0, lwl):
            for j in range(i, lwl):
                if diff(wordList[i], wordList[j]) == 1:
                    g[wordList[i]].add(wordList[j])
                    g[wordList[j]].add(wordList[i])

        for j in range(0, lwl):
            if diff(beginWord, wordList[j]) == 1:
                g[beginWord].add(wordList[j])
                # no returning edge
                pass

        # print(g)
        # do a BFS
        q = deque()
        q.append(beginWord)

        v = defaultdict(bool)
        p = defaultdict(dict)
        p[beginWord] = None

        while q:
            top = q.popleft()
            if top == endWord:
                return len(parent(p, top))

            for el in g[top]:
                if not v[el]:
                    q.append(el)
                    v[el] = True
                    p[el] = top
            # print(q)
        return []


def parent(p, el):
    out = []
    while el:
        out.append(el)
        el = p[el]
    return list(reversed(out))


def diff(a, b):
    ln = len(a)
    count = 0
    for i in range(0, ln):
        if a[i] != b[i]:
            count += 1
    return count


test = False
if test:
    s = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]

    beginWord = "a"
    endWord = "c"
    wordList = ["a", "b", "c"]
    print(s.ladderLength(beginWord, endWord, wordList))
