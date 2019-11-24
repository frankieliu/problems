In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1152.analyze-user-website-visit-pattern.algorithms.json

Python Solution

https://leetcode.com/problems/analyze-user-website-visit-pattern/discuss/355388

* Lang:    python
* Author:  lee215
* Votes:   12

**Python:**
```python
    def mostVisitedPattern(self, username, timestamp, website):
        dp = collections.defaultdict(list)
        for t, u, w in sorted(zip(timestamp, username, website)):
            dp[u].append(w)
        count = sum([collections.Counter(set(itertools.combinations(dp[u], 3))) for u in dp], collections.Counter())
        return list(min(count, key=lambda k: (-count[k], k)))
```

