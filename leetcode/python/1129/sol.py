In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1129.shortest-path-with-alternating-colors.algorithms.json

[Python] BFS

https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339964

* Lang:    python
* Author:  lee215
* Votes:   39

Just need to be noticed that, result can to bigger than `n`.
To be more specific, the maximum result can be `n * 2 - 3`.
So in my solution I initial the result as `n * 2`

Some note:
G = graph
i = index of Node
c = color

**Python:**
```python
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        G = [[[], []] for i in xrange(n)]
        for i, j in red_edges: G[i][0].append(j)
        for i, j in blue_edges: G[i][1].append(j)
        res = [[0, 0]] + [[n * 2, n * 2] for i in xrange(n - 1)]
        bfs = [[0, 0], [0, 1]]
        for i, c in bfs:
            for j in G[i][c]:
                if res[j][c] == n * 2:
                    res[j][c] = res[i][1 - c] + 1
                    bfs.append([j, 1 - c])
        return [x if x < n * 2 else -1 for x in map(min, res)]
```

