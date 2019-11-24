In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1133.largest-unique-number.algorithms.json

C++ O(n), 4 lines

https://leetcode.com/problems/largest-unique-number/discuss/344841

* Lang:    python
* Author:  votrubac
* Votes:   4

```
int largestUniqueNumber(vector<int>& A) {
  short a[1001] = {}, i = 0;
  for (auto n : A) ++a[n];
  for (i = 1000; i >= 0 && a[i] != 1; --i);
  return i;
}
```
