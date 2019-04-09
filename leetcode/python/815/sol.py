
A Different Python BFS Solution - All in a Graph

https://leetcode.com/problems/bus-routes/discuss/256518

* Lang:    python3
* Author:  Lunluen
* Votes:   1

The difference between this solution and the others is:

> You don\'t need to separate the buses from the stops in a graph.

Just put them all in the graph, and you can do BFS as the way you familiar.
Use a negative value to differentiate the buses and stops.

Note: there will be some pits when you try to implement this:
- Stop value could be zero, so you need a `-1` in `bus = -bus - 1` and `<` in `if adj < 0:` rather than `<=`.
- If you use `set` for a `defaultdict`, then you will need   `graph[bus].update(stations)`. But this will consume extra time and memory, so I used `list` and replaced the refereces.

Code:

```Python
import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:
        if S == T: return 0
        
        # Builds graph.
        graph = collections.defaultdict(list)  # Don\'t use set. See below.
        for bus, stops in enumerate(routes):
            bus = -bus - 1  # To avoid conflict with the stops.
            
            # `set.update` consumes extra memory, so a `list` is used instead.
            graph[bus] = stops
            for s in stops:
                graph[s].append(bus)

        # Does BFS.
        dq = collections.deque()
        dq.append((S, 0))
        seen = set([S])
        while dq:
            node, depth = dq.popleft()
            for adj in graph[node]:
                if adj in seen: continue
                if adj == T: return depth
                # If `adj` < 0, it\'s a bus, so we add 1 to `depth`.
                dq.append((adj, depth + 1 if adj < 0 else depth))
                seen.add(adj)
        return -1
```

In 2019/03/17:

> Runtime: 144 ms, faster than 85.42% of Python3 online submissions for Bus Routes.
> Memory Usage: 36.9 MB, less than 57.14% of Python3 online submissions for Bus Routes.
