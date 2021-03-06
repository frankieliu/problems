#
# @lc app=leetcode id=212 lang=python3
#
# [212] Word Search II
#
# https://leetcode.com/problems/word-search-ii/description/
#
# algorithms
# Hard (27.21%)
# Total Accepted:    94.9K
# Total Submissions: 348.6K
# Testcase Example:  '[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]\n["oath","pea","eat","rain"]'
#
# Given a 2D board and a list of words from the dictionary, find all words in
# the board.
#
# Each word must be constructed from letters of sequentially adjacent cell,
# where "adjacent" cells are those horizontally or vertically neighboring. The
# same letter cell may not be used more than once in a word.
#
# Example:
#
#
# Input:
# words = ["oath","pea","eat","rain"] and board =
# [
# ⁠ ['o','a','a','n'],
# ⁠ ['e','t','a','e'],
# ⁠ ['i','h','k','r'],
# ⁠ ['i','f','l','v']
# ]
#
# Output: ["eat","oath"]
#
#
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

from collections import defaultdict


def trie():
    return defaultdict(trie)


class Solution:
    def __init__(self):
        self.t = trie()

    def trieAdd(self, word):
        t = self.t
        for c in word:
            t = t[c]  # this passes a trie
        t['$']  # add end character

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        for w in words:
            self.trieAdd(w)
        self.v = [[False]*len(board[0]) for _ in board]  # visit

        # output
        self.out = set()

        curword = ""
        # for each beginning location
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.findTrie(board, i, j, self.t, curword)
        return list(self.out)

    def findTrie(self, board, i, j, t, curword):
        if '$' in t:
            self.out.add(curword)
            # we don't return here, there might be
            # potentially more solutions

        if (i < 0 or
            i >= len(board) or
            j < 0 or
            j >= len(board[0]) or
            self.v[i][j]):
            return

        c = board[i][j]
        t = t[c]
        if len(t) == 0:
            return

        curword += c
        self.v[i][j] = True
        self.findTrie(board, i+1, j, t, curword[:])
        self.findTrie(board, i-1, j, t, curword[:])
        self.findTrie(board, i, j+1, t, curword[:])
        self.findTrie(board, i, j-1, t, curword[:])
        self.v[i][j] = False


test = True
if test:
    Example = (
        [["o","a","a","n"],
         ["e","t","a","e"],
         ["i","h","k","r"],
         ["i","f","l","v"]],
        ["oath","pea","eat","rain"])
    s = Solution()
    print(s.findWords(Example[0], Example[1]))
