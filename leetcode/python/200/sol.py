
7 lines Python, ~14 lines Java

https://leetcode.com/problems/number-of-islands/discuss/56349

* Lang:    python3
* Author:  StefanPochmann
* Votes:   153

Sink and count the islands.

---

**Python Solution**

    def numIslands(self, grid):
        def sink(i, j):
            if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == '1':
                grid[i][j] = '0'
                map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1))
                return 1
            return 0
        return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

---

**Java Solution 1**

    public class Solution {
        char[][] g;
        public int numIslands(char[][] grid) {
            int islands = 0;
            g = grid;
            for (int i=0; i<g.length; i++)
                for (int j=0; j<g[i].length; j++)
                    islands += sink(i, j);
            return islands;
        }
        int sink(int i, int j) {
            if (i < 0 || i == g.length || j < 0 || j == g[i].length || g[i][j] == '0')
                return 0;
            g[i][j] = '0';
            sink(i+1, j); sink(i-1, j); sink(i, j+1); sink(i, j-1);
            return 1;
        }
    }

---

**Java Solution 2**

    public class Solution {
        public int numIslands(char[][] grid) {
            int islands = 0;
            for (int i=0; i<grid.length; i++)
                for (int j=0; j<grid[i].length; j++)
                    islands += sink(grid, i, j);
            return islands;
        }
        int sink(char[][] grid, int i, int j) {
            if (i < 0 || i == grid.length || j < 0 || j == grid[i].length || grid[i][j] == '0')
                return 0;
            grid[i][j] = '0';
            for (int k=0; k<4; k++)
                sink(grid, i+d[k], j+d[k+1]);
            return 1;
        }
        int[] d = {0, 1, 0, -1, 0};
    }
