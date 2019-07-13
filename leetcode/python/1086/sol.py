In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1086.high-five.algorithms.json

C++ partial sort

https://leetcode.com/problems/high-five/discuss/312426

* Lang:    python
* Author:  Sanzenin_Aria
* Votes:   5

```
    vector<vector<int>> highFive(vector<vector<int>>& items) {
       vector<vector<int>> res;
       map<int, vector<int>> m;
       for (auto& v : items) m[v[0]].push_back(v[1]);
       for (auto& [i, v] : m) {
          partial_sort(v.begin(), v.begin() + 5, v.end(), greater<int>());
          res.push_back({ i, (v[0] + v[1] + v[2] + v[3] + v[4]) / 5 });
       }
       return res;
    }
