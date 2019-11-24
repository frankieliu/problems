In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1108.defanging-an-ip-address.algorithms.json

C++ 1-liner (regex_replace)

https://leetcode.com/problems/defanging-an-ip-address/discuss/328855

* Lang:    python
* Author:  votrubac
* Votes:   15

```
string defangIPaddr(string address) {
  return regex_replace(address, regex("[.]"), "[.]");
}
```
