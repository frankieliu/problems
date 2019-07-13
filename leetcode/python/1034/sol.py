In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1034.coloring-a-border.algorithms.json

C++ with picture, DFS

https://leetcode.com/problems/coloring-a-border/discuss/282847

* Lang:    python
* Author:  votrubac
* Votes:   34

From an initial point, perform DFS and flip the cell color to negative to track visited cells.

After DFS is complete for the cell, check if this cell is inside. If so, flip its color back to the positive.

In the end, cells with the negative color are on the border. Change their color to the target color.
![image](https://assets.leetcode.com/users/votrubac/image_1556425139.png)
```
void dfs(vector<vector<int>>& g, int r, int c, int cl) {
  if (r < 0 || c < 0 || r >= g.size() || c >= g[r].size() || g[r][c] != cl) return;
  g[r][c] = -cl;
  dfs(g, r - 1, c, cl), dfs(g, r + 1, c, cl), dfs(g, r, c - 1, cl), dfs(g, r, c + 1, cl);
  if (r > 0 && r < g.size() - 1 && c > 0 && c < g[r].size() - 1 && cl == abs(g[r - 1][c]) &&
    cl == abs(g[r + 1][c]) && cl == abs(g[r][c - 1]) && cl == abs(g[r][c + 1]))
    g[r][c] = cl;
}
vector<vector<int>> colorBorder(vector<vector<int>>& grid, int r0, int c0, int color) {
  dfs(grid, r0, c0, grid[r0][c0]);
  for (auto i = 0; i < grid.size(); ++i)
    for (auto j = 0; j < grid[i].size(); ++j) grid[i][j] = grid[i][j] < 0 ? color : grid[i][j];
  return grid;
}
```
