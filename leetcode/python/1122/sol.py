In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1122.relative-sort-array.algorithms.json

Python Straight Forward Solution

https://leetcode.com/problems/relative-sort-array/discuss/334585

* Lang:    python
* Author:  lee215
* Votes:   31

```
def relativeSortArray(self, A, B):
        k = {v: i for i, v in enumerate(B)}
        return sorted(A, key=lambda i: k.get(i, 1000 + i))
