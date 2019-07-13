In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1101.the-earliest-moment-when-everyone-become-friends.algorithms.json

[Python] Union-Find

https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/discuss/322961

* Lang:    python
* Author:  lee215
* Votes:   5

**Python:**
```python
    def earliestAcq(self, logs, N):
        uf = {x: x for x in xrange(N)}
        self.groups = N

        def merge(x, y):
            x, y = find(x), find(y)
            if x != y:
                self.groups -= 1
                uf[x] = y

        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for t, x, y in sorted(logs):
            merge(x, y)
            if self.groups == 1:
                return t
        return -1
```

