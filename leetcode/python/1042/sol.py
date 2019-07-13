In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1042.flower-planting-with-no-adjacent.algorithms.json

[Java/C++/Python] Greedily Paint

https://leetcode.com/problems/flower-planting-with-no-adjacent/discuss/290858

* Lang:    python
* Author:  lee215
* Votes:   59

## **Intuition**
Greedily paint nodes one by one.
Because there is no node that has more than 3 neighbors,
always one possible color to choose.

## **Complexity**
Time `O(N)` with `O(paths) = O(1.5N)`
Space `O(N)`


**Java**
```
    public int[] gardenNoAdj(int N, int[][] paths) {
        Map<Integer, Set<Integer>> G = new HashMap<>();
        for (int i = 0; i < N; i++) G.put(i, new HashSet<>());
        for (int[] p : paths) {
            G.get(p[0] - 1).add(p[1] - 1);
            G.get(p[1] - 1).add(p[0] - 1);
        }
        int[] res = new int[N];
        for (int i = 0; i < N; i++) {
            int[] colors = new int[5];
            for (int j : G.get(i))
                colors[res[j]] = 1;
            for (int c = 4; c > 0; --c)
                if (colors[c] == 0)
                    res[i] = c;
        }
        return res;
    }
```
**C++**
```
    vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
        vector<int> res(N);
        vector<vector<int>> G(N);
        for (vector<int>& p : paths) {
            G[p[0] - 1].push_back(p[1] - 1);
            G[p[1] - 1].push_back(p[0] - 1);
        }
        for (int i = 0; i < N; ++i) {
            int colors[5] = {};
            for (int j : G[i])
                colors[res[j]] = 1;
            for (int c = 4; c > 0; --c)
                if (!colors[c])
                    res[i] = c;
        }
        return res;
    }
```
**Python:**
```
    def gardenNoAdj(self, N, paths):
        res = [0] * N
        G = [[] for i in range(N)]
        for x, y in paths:
            G[x - 1].append(y - 1)
            G[y - 1].append(x - 1)
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res
```

