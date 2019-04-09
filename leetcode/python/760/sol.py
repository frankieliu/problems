
Support unique index when duplicated (one-to-one map version)

https://leetcode.com/problems/find-anagram-mappings/discuss/247097

* Lang:    python3
* Author:  sevenhe716
* Votes:   0

I know there is no requirement for the indice mappings to be distinct.
But if you want one-to-one map version (in my understanding), here is the solution:

```
def anagramMappings(self, A: \'List[int]\', B: \'List[int]\') -> \'List[int]\':
	b_idx = defaultdict(list)
	for i, b in enumerate(B):
		b_idx[b].append(i)
	return list(map(lambda x: b_idx[x].pop(), A))
```
