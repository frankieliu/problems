In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1154.day-of-the-year.algorithms.json

C++, Number of Days in a Month

https://leetcode.com/problems/day-of-the-year/discuss/355916

* Lang:    python
* Author:  votrubac
* Votes:   12

We need to sum the number of days in previous months, so we build on top of [1118. Number of Days in a Month](https://leetcode.com/problems/number-of-days-in-a-month/).

Note that we need to add one day for February for a leap year.
```
int days[12] = { 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
int dayOfYear(string dt) {
  int y = stoi(dt.substr(0, 4)), m = stoi(dt.substr(5, 2)), d = stoi(dt.substr(8));
  if (m > 2 && y % 4 == 0 && (y % 100 != 0 || y % 400 == 0)) ++d; 
  while (--m > 0) d += days[m - 1];
  return d;
}
```
