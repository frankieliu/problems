
Python Simple Dijkstra

https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/238116

* Lang:    python3
* Author:  leonmak
* Votes:   1

```py
def findCheapestPrice(self, n, flights, src, dst, K):
	"""
	:type n: int
	:type flights: List[List[int]]
	:type src: int
	:type dst: int
	:type K: int
	:rtype: int
	"""
	# construct graph
	graph = defaultdict(list)
	for u, v, w in flights:
		graph[u].append((v, w))

	# dist, idx, path_len
	q = [(0, src, 1)]
	max_path_len = K + 2
	while q:
		dist, idx, path_len = heappop(q)
		if path_len > max_path_len:
			continue
		if idx == dst:
			return dist
		for v, w in graph[idx]:
			heappush(q, (dist+w, v, path_len+1))
	return -1
```
