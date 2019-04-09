
Simple dfs, python beat 100%

https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/237372

* Lang:    python3
* Author:  leonmak
* Votes:   0

```
def depthSumInverse(self, nestedList):
	"""
	:type nestedList: List[NestedInteger]
	:rtype: int
	"""
	self.max_h = 0
	res = []  # (depth, val)

	def dfs(node, depth):
		if not node:
			return
		self.max_h = max(self.max_h, depth)
		if not node.isInteger():
			n_d = depth+1
			for n_i in node.getList():
				dfs(n_i, n_d)
		else:
			res.append((depth, node.getInteger()))

	for node in nestedList:
		dfs(node, 0)
	w = 0
	for dep, val in res:
		w += (self.max_h-dep+1) * val
	return w
```
