In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1029.two-city-scheduling.algorithms.json

C++ O(n log n) sort by savings

https://leetcode.com/problems/two-city-scheduling/discuss/278716

* Lang:    python
* Author:  votrubac
* Votes:   82

# Intuition
How much money can we save if we fly a person to A vs. B? To minimize the total cost, we should fly the person with the maximum saving to A, and with the minimum - to B.

Example: [30, 100], [40, 90], [50, 50], [70, 50].
Savings: 70, 50, 0, -20.

Obviously, first person should fly to A, and the last - to B.
# Solution
We sort the array by the difference between costs for A and B. Then, we fly first ```N``` people to A, and the rest - to B.
```
int twoCitySchedCost(vector<vector<int>>& cs, int res = 0) {
  sort(begin(cs), end(cs), [](vector<int> &v1, vector<int> &v2) {
    return (v1[0] - v1[1] < v2[0] - v2[1]);
  });
  for (auto i = 0; i < cs.size() / 2; ++i) {
    res += cs[i][0] + cs[i + cs.size() / 2][1];
  }
  return res;
}
```
# Optimized Solution
Actually, we do not need to perfectly sort all cost differences, we just need the biggest savings (to fly to A) to be in the first half of the array. So, we can use the quick select algorithm (```nth_element``` in C++) and use the middle of the array as a pivot. 

This brings the runtime down from 8 ms to 4 ms (thanks [@popeye1](https://leetcode.com/popeye1/) for the tip!)
```
int twoCitySchedCost(vector<vector<int>>& cs, int res = 0) {
  nth_element(begin(cs), begin(cs) + cs.size() / 2, end(cs), [](vector<int> &a, vector<int> &b) {
    return (a[0] - a[1] < b[0] - b[1]);
  });
  for (auto i = 0; i < cs.size() / 2; ++i) {
    res += cs[i][0] + cs[i + cs.size() / 2][1];
  }
  return res;
}
```
# Complexity Analysis
Runtime: *O(n log n)*. We sort the array then go through it once. The second solution has a better average case runtime.
Memory: *O(1)*. We sort the array in-place.
