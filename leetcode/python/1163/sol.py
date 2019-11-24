In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1163.last-substring-in-lexicographical-order.algorithms.json

Why Brute Force is Passing Successfully?

https://leetcode.com/problems/last-substring-in-lexicographical-order/discuss/360994

* Lang:    python
* Author:  sourov_roy
* Votes:   47

Why it is a Hard Problem, if Brute Force is passing successfully?

```
def lastSubstring(self, s):
        result=""
        for i in range(len(s)):
            result=max(result,s[i:])
        return result
```

Edit : The testcases are now fixed.

