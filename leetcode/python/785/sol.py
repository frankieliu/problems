
Readable Python

https://leetcode.com/problems/is-graph-bipartite/discuss/253757

* Lang:    python3
* Author:  etherealoptimist
* Votes:   0

```
from collections import defaultdict
def isBipartite(self, graph):
	color = defaultdict(int)
	def dfs(cur):
		for neighbor in graph[cur]:
			if neighbor in color:
				if color[cur] == color[neighbor]:
					return False
			else:
				color[neighbor] = ~color[cur]
				if not dfs(neighbor):
					return False
		return True

	for node, _ in enumerate(graph):
		if not dfs(node):
			return False
	return True
```
