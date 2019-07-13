In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1091.shortest-path-in-binary-matrix.algorithms.json

C++ BFS

https://leetcode.com/problems/shortest-path-in-binary-matrix/discuss/312711

* Lang:    python
* Author:  votrubac
* Votes:   9

BFS gives us the shortest path, so we will just do that.
```
int shortestPathBinaryMatrix(vector<vector<int>>& g, int steps = 0) {
  queue<pair<int, int>> q;
  q.push({ 0, 0 });
  while (!q.empty()) {
    ++steps;
    queue<pair<int, int>> q1;
    while (!q.empty()) {
      auto c = q.front();
      q.pop();
      if (c.first >= 0 && c.second >= 0 && c.first < g.size() && c.second < g.size() && !g[c.first][c.second]) {
        g[c.first][c.second] = 1;
        if (c.first == g.size() - 1 && c.second == g.size() - 1) return steps;
        for (auto i = -1; i < 2; ++i)
          for (auto j = -1; j < 2; ++j)
            if (i != 0 || j != 0) q1.push({ c.first + i, c.second + j });
      }
    }
    swap(q, q1);
  }
  return -1;
}
```
We can also check the coordinates before adding them to the queue; it can save some memory and runtinme:
```
int shortestPathBinaryMatrix(vector<vector<int>>& g, int steps = 0) {
  queue<pair<int, int>> q;
  q.push({ 0, 0 });
  while (!q.empty()) {
    ++steps;
    queue<pair<int, int>> q1;
    while (!q.empty()) {
      auto c = q.front();
      q.pop();
      if (exchange(g[c.first][c.second], 1) == 1) continue;
      if (c.first == g.size() - 1 && c.second == g.size() - 1) return steps;
      for (auto i = c.first - 1; i <= c.first + 1; ++i)
        for (auto j = c.second - 1; j <= c.second + 1; ++j)
          if (i != c.first || j != c.second) {
            if (i >= 0 && j >= 0 && i < g.size() && j < g.size() && !g[i][j]) {
              q1.push({ i, j });
            }
          }
    }
    swap(q, q1);
  }
  return -1;
}
```
