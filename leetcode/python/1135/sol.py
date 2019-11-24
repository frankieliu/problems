In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1135.connecting-cities-with-minimum-cost.algorithms.json

Java Kruskal’s Minimum Spanning Tree Algorithm with Union Find

https://leetcode.com/problems/connecting-cities-with-minimum-cost/discuss/344867

* Lang:    python
* Author:  yuanb10
* Votes:   9

We use Kruskal\u2019s algorithm to generate a minimum spanning tree for the graph. Use Union-Find to detect cycle.

Idea is simple:
1. Sort edges to no-descresing order
2. Pick the smallest edge that does not form a cycle
3. Repeat until MST is formed and every node is connected.

Implemented Union-Find with path comression to improve efficiency. 

There are tons of materials online about the proof of correctness and analysis of this algorithm. Feel free to check them around.

Hope this helps.

```
class Solution {
    
    int[] parent;
    int n;
    
    private void union(int x, int y) {
        int px = find(x);
        int py = find(y);
        
        if (px != py) {
            parent[px] = py;
            n--;
        }
    }
    
    private int find(int x) {
        if (parent[x] == x) {
            return parent[x];
        }
        parent[x] = find(parent[x]); // path compression
        return parent[x];
    }
    
    public int minimumCost(int N, int[][] connections) {
        parent = new int[N + 1];
        n = N;
        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }
        
        Arrays.sort(connections, (a, b) -> (a[2] - b[2]));
        
        int res = 0;
        
        for (int[] c : connections) {
            int x = c[0], y = c[1];
            if (find(x) != find(y)) {
                res += c[2];
                union(x, y);
            }
        }
        
        return n == 1 ? res : -1;
    }
}
```
