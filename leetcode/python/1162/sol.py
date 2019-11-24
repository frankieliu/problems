In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1162.as-far-from-land-as-possible.algorithms.json

C++ with picture, DFS and BFS

https://leetcode.com/problems/as-far-from-land-as-possible/discuss/360963

* Lang:    python
* Author:  votrubac
* Votes:   58

# Intution
Normally, we would run breadth-first search from each cell simultaneonly, tracking water cells we visited. Sort of like Dijkastra\u2019s algorithm. However, I wanted to try a depth-first search solution, as it seemed easier to implement at the time.

The DFS solution is accepted but has higher runtime complexity, so I then added the BFS solution to compare.
# DFS Solution
For each \'land\' cell, start DFS and record the distance in \'water\' cells.

If the distance in the \'water\' cell is smaller than the current distance, we stop there. Otherwise, we update the distance to the smaller value and keep going.

So our grid will have the following values:
- ```1``` for land
- ```0``` for water
- ```>=2``` water with the recorded distance

In the end, we scan the grid again and returning the largest value.

In this example, the cells contains distances after DFS is complete for each land cell. In the end, the maximum distance from the land is 3 (4 - 1).
![image](https://assets.leetcode.com/users/votrubac/image_1566199200.png)
```
void dfs(vector<vector<int>>& g, int i, int j, int dist, bool land = false) {
  if (!land) {
    if (i < 0 || j < 0 || i >= g.size() || j >= g[i].size() || (g[i][j] != 0 && g[i][j] <= dist)) return;
    g[i][j] = dist;
  }
  dfs(g, i - 1, j, dist + 1), dfs(g, i + 1, j, dist + 1), dfs(g, i, j - 1, dist + 1), dfs(g, i, j + 1, dist + 1);
}
int maxDistance(vector<vector<int>>& g, int mx = -1) {
  for (auto i = 0; i < g.size(); ++i)
    for (auto j = 0; j < g[i].size(); ++j)
      if (g[i][j] == 1) dfs(g, i, j, 1, true);
  for (auto i = 0; i < g.size(); ++i)
    for (auto j = 0; j < g[i].size(); ++j)
      if (g[i][j] > 1) mx = max(mx, g[i][j] - 1);
  return mx;
}
```
## Complexity Analysis
Runtime: O(m * n * n), where m is the number of land cells.
Memory: O(n) for the recursion.
# BFS Solution
The solution above is slow, and BFS can help to make sure we process a single cell only once (well, twice in our case to scan for the land first).

Here, we find our land cells and put surrounding water cells in the queue. We mark water cells as visited and continue the expansion from land cells until there are no more water cells left. In the end, the number of steps in DFS is how far can we go from the land.

Using the same example as above, the picture below shows the state of the grid after each step of BFS.
![image](https://assets.leetcode.com/users/votrubac/image_1566199213.png)
```
int maxDistance(vector<vector<int>>& g, int steps = 0) {
  queue<pair<int, int>> q, q1;
  for (auto i = 0; i < g.size(); ++i)
    for (auto j = 0; j < g[i].size(); ++j)
      if (g[i][j] == 1)
        q.push({ i - 1, j }), q.push({ i + 1, j }), q.push({ i, j - 1 }), q.push({ i, j + 1 });
  while (!q.empty()) {
    ++steps;
    while (!q.empty()) {
      int i = q.front().first, j = q.front().second;
      q.pop();
      if (i >= 0 && j >= 0 && i < g.size() && j < g[i].size() && g[i][j] == 0) {
        g[i][j] = steps;
        q1.push({ i - 1, j }), q1.push({ i + 1, j }), q1.push({ i, j - 1 }), q1.push({ i, j + 1 });
      }
    }
    swap(q1, q);
  }
  return steps == 1 ? -1 : steps - 1;
}
```
## Complexity Analysis
Runtime: O(n * n). We process an individual cell only once (or twice).
Memory: O(n) for the queue.
