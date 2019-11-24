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
from collections import defaultdict


class Solution:
    def findLadders(self, beginWord, endWord, wl):

        def one_away(a, b):
            count = 0
            for i in range(0, len(a)):
                if a[i] != b[i]:
                    count += 1
                if count > 1:
                    break
            return count == 1

        def dfs(a, count, gcount, visited, target):
            # print("a{} count{} gcount{} visited{} target{}".
            #  format(a, count, gcount, visited, target))
            if count > gcount[0]:
                return None
            if a == target:
                gcount[0] = count
                return [[a]]
            nei = n[a] - visited
            out = []
            for b in nei:
                visited.add(b)
                res = dfs(b, count + 1, gcount, visited, target)
                if res:
                    for r in res:
                        r.append(a)
                    out.extend(res)
                visited.remove(b)
            return out

        def towords(ilist, wl):
            return [wl[i] for i in ilist]

        gcount = [len(wl)]
        n = defaultdict(set)
        for i in range(0, len(wl)):
            for j in range(i, len(wl)):
                if one_away(wl[i], wl[j]):
                    n[i].add(j)
                    n[j].add(i)

        out = []
        if endWord not in wl:
            return []
        target = wl.index(endWord)
        visited = set()
        for i in range(0, len(wl)):
            if one_away(beginWord, wl[i]):
                visited.add(i)
                res = dfs(i, 1, gcount, visited, target)
                if res:
                    out.extend(res)
                visited.remove(i)

        # filter by smallest
        out = [[beginWord] + towords(reversed(x),wl) for x in out if len(x) == gcount[0]]
        return out


test = True
if test:
    s = Solution()
    case = [False]*0 + [True] + [False]*2
    if case[0]:
        # Example 1:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
        # Output:
        # Output:
        # [
        # ⁠ ["hit","hot","dot","dog","cog"],
        #  ["hit","hot","lot","log","cog"]
        # ]
        print(s.findLadders(beginWord, endWord, wordList))

    if case[1]:
        # Example 2:
        beginWord = "hit"
        endWord = "cog"
        wordList = ["hot", "dot", "dog", "lot", "log"]
        # Output: []
        print(s.findLadders(beginWord, endWord, wordList))
