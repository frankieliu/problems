
Python 52ms DFS Algorithm with Explanations (compared with 52ms union-find)

https://leetcode.com/problems/redundant-connection/discuss/107990

* Lang:    python3
* Author:  flamesofmoon
* Votes:   13

The algorithm based on the following fact in graph theory:

**a simple connected graph with no cycle is a tree**.

The statement of the problem guarantees that by deleting one and only one edge the graph is a tree, so we know it is connected and has one cycle. Our goal is to find the edge in this cycle with the largest index and return it.

How? DFS!

We store the graph in a dictionary `e` so that we can easily find adjacent vertices. `indices` helps me keep track of the original indices of edges in `edges`. `path` is to record the fact that we arrive at a vertex `v` from `path[v]`.

When constructing `e`, we already get rid of the 2-cycle case by
```
            if p[1] in e[p[0]]:
                return p
```
so in DFS, we only focus on cycles whose length >= 3. Since the graph is connected, we will find the cycle wherever we start. Pick one randomly (i.e., `e.keys()[0]`) and set off!

In `DFS(v)`: 
1) Look at all vertices 'w' adjacent to v such that the predecessor of `v` in DFS path is not `w` (otherwise it would be a two-vertex infinite loop, and we know there is no 2-cycle).

2) If `path[w] != 0`, means `w` is on the current DFS path! The cycle is found and just need to make the change `path[w] = v` to complete the cycle and return the result.

3) Standard DFS things: we record down the path in `path` and after DFS change it back to 0 state.

4) It is possible that the DFS path goes into a dead end, so in a branch of DFS, it is possible that nothing is returned. We respect this possibility and do the check
```
                temp = DFS(w)
                if temp:
                    return temp
```
The function `Result` is just a practice of typing once we have `indices` which indicates the corresponding indices for edges.

My thought is pretty natural besides the fact that for this problem union-find is a method much easier to type up (and could be as fast). Anyway, here is my DFS algorithm:

```
        def Result(w):  # given w is a vertex in a cycle, find the edge with the largest index in this cycle
            prev, curr =w, path[w]
            M = indices[(curr, prev)]
            while curr != w:
                prev, curr = curr, path[curr]
                M = max(M,indices[(curr, prev)])

            return edges[M]
        
        def DFS(v):
            for w in e[v]:
                if path[v] == w:  # if predecessor of v is w, it's bad
                    continue

                if path[w] != 0:  # the cycle is found
                    path[w] = v   # complete the cycle
                    return Result(w)

                path[w] = v
                temp = DFS(w)
                if temp:          # in case it is a dead end and returns nothing
                    return temp
                path[w] = 0
        
        e = collections.defaultdict(set)  # e[x] is the set of all vertices adjacent to x
        indices = {}                      # key is edge, value is indices in the list 'edges'
        for i,p in enumerate(edges):
            if p[1] in e[p[0]]:
                return p                  # if one edge appears twice in 'edges', return tha latter one
            e[p[0]].add(p[1])
            e[p[1]].add(p[0])
            indices[(p[0],p[1])] = indices[(p[1],p[0])] = i

        path = {x:0 for x in e}           # record the path in DFS
        return DFS(e.keys()[0])
```
My union-find algorithm with best time performance:
```
        def find(v):                         # find the root of the tree
            return find(parent[v]) if v in parent else v

        parent = {}                          # record the child: parent relation in the forest
        for i,p in enumerate(edges):
            r1, r2 = map(find, p)
            if r1 == r2:
                return p
            else:
                parent[r1] = parent[r2] = str(i) # use str(i) as the tree label
```
