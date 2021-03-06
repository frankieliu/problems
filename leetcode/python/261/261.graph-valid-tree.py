#
# @lc app=leetcode id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.com/problems/graph-valid-tree/description/
#
# algorithms
# Medium (39.52%)
# Total Accepted:    83.4K
# Total Submissions: 211.1K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge
# is a pair of nodes), write a function to check whether these edges make up a
# valid tree.
#
# Example 1:
#
#
# Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
# Output: true
#
# Example 2:
#
#
# Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
# Output: false
#
# Note: you can assume that no duplicate edges will appear in edges. Since all
# edges are undirected, [0,1] is the same as [1,0] and thus will not appear
# together in edges.
#
#
from collections import defaultdict


class Solution:

    def __init__(self):
        self.visited = set()

    def validTree(self, n, edges):
        """
        a valid tree doesn't contain a cycle
        and no unreachable nodes
        """
        if n == 1:
            return True

        if len(edges) == 0:
            return False

        self.g = defaultdict(list)
        for a, b in edges:
            self.g[a].append(b)
            self.g[b].append(a)

        cycle = self.dfs(edges[0][0])
        if cycle:
            # print("Found a cycle")
            return False

        if n != len(self.visited):
            return False

        return True

    def dfs(self, n):
        self.visited.add(n)
        # print("dfs{}".format(n))
        for i in self.g[n]:
            # delete backward edge
            self.g[i].remove(n)
            if i in self.visited:
                return True
            else:
                if self.dfs(i):
                    return True
        return False


test = True
if test:
    s = Solution()
    case = [False, False, False, True]
    if case[0]:
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        # Output: true
        print(s.validTree(n, edges))
    if case[1]:
        n = 5
        edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
        # Output: false
        print(s.validTree(n, edges))
    if case[2]:
        n = 2
        edges = []
        print(s.validTree(n, edges))
    if case[3]:
        n = 3
        edges = [[1,0]]
        print(s.validTree(n, edges))
