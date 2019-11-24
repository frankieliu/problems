In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1168.optimize-water-distribution-in-a-village.algorithms.json

[C++/Python/Java] Hidden Well in House 0

https://leetcode.com/problems/optimize-water-distribution-in-a-village/discuss/365853

* Lang:    python
* Author:  lee215
* Votes:   38

## **Intuition**
I take it this way:
We cannot build any well.
There is one and only one hidding well in my house (house 0).
The cost to lay pipe between `house[i]` and my house is `wells[i]`.

In order to supply water to the whole village,
we need to make the village a coonected graph.
<br>

## **Explanation**
Merge all costs of pipes together and sort by key.
Greedily lay the pipes if it can connect two seperate union.
Appply union find to record which houses are connected.
<br>

## **Complexity**
Time `O(ElogE)`
Space `O(N)`
<br>


**C++**
```cpp
    vector<int> uf;
    int minCostToSupplyWater(int n, vector<int>& wells, vector<vector<int>>& pipes) {
        uf.resize(n + 1, 0);
        for (auto& p : pipes) swap(p[0], p[2]);
        for (int i = 0; i < n; ++i) {
            uf[i + 1] = i + 1;
            pipes.push_back({wells[i], 0, i + 1});
        }
        sort(pipes.begin(), pipes.end());

        int res = 0;
        for (int i = 0; n > 0; ++i) {
            int x = find(pipes[i][1]), y = find(pipes[i][2]);
            if (x != y) {
                res += pipes[i][0];
                uf[x] = y;
                --n;
            }
        }
        return res;
    }

    int find(int x) {
        if (x != uf[x]) uf[x] = find(uf[x]);
        return uf[x];
    }
```

**Python:**
```python
    def minCostToSupplyWater(self, n, wells, pipes):
        uf = {i: i for i in xrange(n + 1)}

        def find(x):
            if x != uf[x]:
                uf[x] = find(uf[x])
            return uf[x]

        w = [[c, 0, i] for i, c in enumerate(wells, 1)]
        p = [[c, i, j] for i, j, c in pipes]
        res = 0
        for c, x, y in sorted(w + p):
            x, y = find(x), find(y)
            if x != y:
                uf[find(x)] = find(y)
                res += c
                n -= 1
            if n == 0:
                return res
```

**Java**
```java
    int[] uf;
    public int minCostToSupplyWater(int n, int[] wells, int[][] pipes) {
        uf = new int[n + 1];
        List<int[]> edges = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            uf[i + 1] = i + 1;
            edges.add(new int[] {0, i + 1, wells[i]});
        }
        for (int[] p : pipes) {
            edges.add(p);
        }
        Collections.sort(edges, (a, b) -> Integer.compare(a[2], b[2]));

        int res = 0;
        for (int[] e : edges) {
            int x = find(e[0]), y = find(e[1]);
            if (x != y) {
                res += e[2];
                uf[x] = y;
                --n;
            }
        }
        return res;
    }

    private int find(int x) {
        if (x != uf[x]) uf[x] = find(uf[x]);
        return uf[x];
    }
```
