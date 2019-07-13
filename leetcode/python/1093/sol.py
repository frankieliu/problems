In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1093.statistics-from-a-large-sample.algorithms.json

Python Solution

https://leetcode.com/problems/statistics-from-a-large-sample/discuss/317626

* Lang:    python
* Author:  lee215
* Votes:   17

**Python:**
```
    def sampleStats(self, count):
        n = sum(count)
        mi = next(i for i in xrange(256) if count[i]) * 1.0
        ma = next(i for i in xrange(255, -1, -1) if count[i]) * 1.0
        mean = sum(i * v for i, v in enumerate(count)) * 1.0 / n
        mode = count.index(max(count)) * 1.0
        for i in xrange(255):
            count[i + 1] += count[i]
        median1 = bisect.bisect(count, (n - 1) / 2)
        median2 = bisect.bisect(count, n / 2)
        median = (median1 + median2) / 2.0
        return [mi, ma, mean, median, mode]
```
