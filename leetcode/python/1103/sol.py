In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1103.distribute-candies-to-people.algorithms.json

C++ brute-force

https://leetcode.com/problems/distribute-candies-to-people/discuss/323298

* Lang:    python
* Author:  votrubac
* Votes:   13

I was going down the mathematical path and it felt a bit tricky. Since the problem is \'Easy\', I guessed the brute-force should do for the contest.
```
vector<int> distributeCandies(int c, int num) {
  vector<int> res(num);
  for (auto i = 0; c > 0; c -= ++i) 
    res[i % num] += min(i + 1, c);
  return res;
}
```
