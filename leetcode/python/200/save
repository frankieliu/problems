#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#
# https://leetcode.com/problems/number-of-islands/description/
#
# algorithms
# Medium (39.81%)
# Total Accepted:    287K
# Total Submissions: 720.8K
# Testcase Example:  '[["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]'
#
# Given a 2d grid map of '1's (land) and '0's (water), count the number of
# islands. An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all four edges of
# the grid are all surrounded by water.
#
# Example 1:
#
#
# Input:
# 11110
# 11010
# 11000
# 00000
#
# Output: 1
#
#
# Example 2:
#
#
# Input:
# 11000
# 11000
# 00100
# 00011
#
# Output: 3
#
#
class Solution:
    """

    For a single row it is pretty easy to count the number of islands
    - just iterate through the array and check if previous element was an
      island or not, if not then it is a new island

    Main idea here is to merge the rows together if islands intersect
    from other rows:
    - if there are two or more islands from above they get merged if
      there is a slab below which connects them together

    Use a hash to keep the number of active islands.

    New islands get new labels via a count.  Even if islands are later
    merged we still keep increment count, and just delete the element in
    the hash to indicate that the island has merged

    To disambiguate which label to keep during merge, we always choose the
    smallest label.

    """

    def numIslands(self, grid):
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        p = {}

        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px < py:
                p[py] = px
            else:
                p[px] = py

        nr = len(grid)
        nc = len(grid[0])
        print(nr, nc)
        for row in range(nr):
            for col in range(nc):
                if grid[row][col] == "1":
                    id = row * nc + col
                    p[row * nc + col] = row * nc + col
                    if col != 0:
                        if grid[row][col - 1] == "1":
                            union(id - 1, id)
                    if row != 0:
                        if grid[row - 1][col] == "1":
                            union(id - nc, id)
        for i in p:
            find(i)
        return len(set(p.values()))


test = True
if test:
    s = Solution()
    case = [False] * 4 + [True] * 1 + [False] * 10
    if case[0]:
        a = ["11110", "11010", "11000", "00000"]
        print(s.numIslands(a))
    if case[1]:
        a = ["11000", "11000", "00100", "00011"]
        print(s.numIslands(a))
    if case[2]:
        a = [["1", "0", "1", "1", "0", "1", "1"]]
        print(s.numIslands(a))
    if case[3]:
        a = [["1", "1", "1", "1", "1", "1",
              "1"], ["0", "0", "0", "0", "0", "0",
                     "1"], ["1", "1", "1", "1", "1", "0",
                            "1"], ["1", "0", "0", "0", "1", "0",
                                   "1"], ["1", "0", "1", "0", "1", "0", "1"],
             ["1", "0", "1", "1", "1", "0",
              "1"], ["1", "1", "1", "1", "1", "1", "1"]]
        print(s.numIslands(a))
    if case[4]:
        a = [["1", "0", "1", "1", "1"], ["1", "0", "1", "0", "1"],
             ["1", "1", "1", "0", "1"]]
        print(s.numIslands(a))
