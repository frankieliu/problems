#
# @lc app=leetcode id=1048 lang=python
#
# [1048] Longest String Chain
#
# https://leetcode.com/problems/longest-string-chain/description/
#
# algorithms
# Medium (47.24%)
# Total Accepted:    7.1K
# Total Submissions: 15K
# Testcase Example:  '["a","b","ba","bca","bda","bdca"]'
#
# Given a list of words, each word consists of English lowercase letters.
#
# Let's say word1 is a predecessor of word2 if and only if we can add exactly
# one letter anywhere in word1 to make it equal to word2.  For example, "abc"
# is a predecessor of "abac".
#
# A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >=
# 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of
# word_3, and so on.
#
# Return the longest possible length of a word chain with words chosen from the
# given list of words.
#
#
#
# Example 1:
#
#
# Input: ["a","b","ba","bca","bda","bdca"]
# Output: 4
# Explanation: one of the longest word chain is "a","ba","bda","bdca".
#
#
#
#
# Note:
#
#
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 16
# words[i] only consists of English lowercase letters.
#
#
#
#
#
#
from collections import defaultdict
class Solution(object):
    def longestStrChain(self, words):
        def connected(a,b):
            err = 0
            i = 0
            while i < len(a):
                if a[i] != b[i+err]:
                   err += 1
                   if err > 1:
                       return False
                else:
                    i += 1
            return True
        g = defaultdict(list)
        indegree = [0]*len(words)
        for i in range(len(words)):
            for j in range(i+1,len(words)):
               if abs(len(words[i]) - len(words[j])) == 1:
                   small, large = i,j
                   if len(words[i]) > len(words[j]):
                       small,large = large,small
                   if connected(words[small],words[large]):
                       g[small].append(large)
                       indegree[large] += 1
                       # print(words[small],words[large])
        # print(g)
        unvisited = set(range(len(words)))
        res = 0
        while unvisited:
            res += 1
            degree0 = [x for x in unvisited if indegree[x] == 0]
            for i in degree0:
                if indegree[i] == 0:
                    unvisited.remove(i)
                    for j in g[i]:
                        indegree[j] -= 1
        return res
test = True
if test:
    sol = Solution()
    case = [False]*2 + [True] + [False]*1
    if case[0]:
        # Example 1:
        Input = ["a","b","ba","bca","bda","bdca"]
        # Output: 4
        print(sol.longestStrChain(Input))
    if case[1]:
        testcase = ["ksqvsyq","ks","kss","czvh","zczpzvdhx","zczpzvh","zczpzvhx","zcpzvh","zczvh","gr","grukmj","ksqvsq","gruj","kssq","ksqsq","grukkmj","grukj","zczpzfvdhx","gru"]
        print(sol.longestStrChain(testcase))
    if case[2]:
        testcase = ["qyssedya","pabouk","mjwdrbqwp","vylodpmwp","nfyqeowa","pu","paboukc","qssedya","lopmw","nfyqowa","vlodpmw","mwdrqwp","opmw","qsda","neo","qyssedhyac","pmw","lodpmw","mjwdrqwp","eo","nfqwa","pabuk","nfyqwa","qssdya","qsdya","qyssedhya","pabu","nqwa","pabqoukc","pbu","mw","vlodpmwp","x","xr"]
        print(sol.longestStrChain(testcase))
