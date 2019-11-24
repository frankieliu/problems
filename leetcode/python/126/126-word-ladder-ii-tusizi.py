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


#https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        if endWord not in wordList or not endWord or not beginWord:
            return []
        wordList = set(wordList)
        forward, backward = {beginWord}, {endWord}
        direction = 1
        parents = collections.defaultdict(set)
        while forward and backward:
            if len(forward) > len(backward):
                forward, backward = backward, forward
                direction *= -1
            next_forward = set()
            wordList -= forward
            for word in forward:
                for i in range(len(word)):
                    first, second = word[:i], word[i+1:]
                    for ch in string.ascii_lowercase:
                        combined_word = first + ch + second
                        if combined_word in wordList:
                            next_forward.add(combined_word)
                            if direction == 1:
                                parents[combined_word].add(word)
                            else:
                                parents[word].add(combined_word)
            if next_forward & backward:
                self.res = []
                path = [endWord]
                self.dfs(parents, endWord, beginWord,path)
                return self.res
            forward = next_forward
        return []
    def dfs(self,parents,cur_w,beginWord,path):
        if cur_w == beginWord:
            self.res.append(path[::-1])
            return
        for eword in parents[cur_w]:
            path.append(eword)
            self.dfs(parents,eword,beginWord,path)
            path.pop()


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
