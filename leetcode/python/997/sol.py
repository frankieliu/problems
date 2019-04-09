
Python - O(n) with Explanation

https://leetcode.com/problems/find-the-town-judge/discuss/244859

* Lang:    python3
* Author:  alices
* Votes:   6

Keep track of the cumulative score of each person: if person a trusts person b, we decrement a\'s score and increment b\'s score. 
**The judge is the only person that ends up with a score of N-1.**

I initialize the trusted list with N+1 items to make indexing easier, since the villagers are named 1 thorugh N. 

**Time complexity** O(N + T): T=len(trust). We iterate through the trust list once and through all villagers once, so the time complexity is linear in these. This is equivalent to |Vertices| + |Edges| in graph terms, if we consider each person as a vertex and each trust relationship as a directed edge. 

**Space complexity** O(N): We create a trusted list with a size of N+1 to store the cumulative scores.

```
def findJudge(self, N, trust):
	trusted = [0] * (N+1)
	for a, b in trust:
		trusted[a] -= 1
		trusted[b] += 1

	for i in range(1, N+1):
		if trusted[i] == N-1:
			return i
	return -1
```
