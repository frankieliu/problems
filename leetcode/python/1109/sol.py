In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1109.corporate-flight-bookings.algorithms.json

C++/Java with picture, O(n)

https://leetcode.com/problems/corporate-flight-bookings/discuss/328871

* Lang:    python
* Author:  votrubac
* Votes:   110

# Intuition
Since ranges are continuous, what if we add reservations to the first flight in the range, and remove them after the last flight in range? We can then use the running sum to update reservations for all flights.

This picture shows the logic for this test case: ```[[1,2,10],[2,3,20],[3,5,25]]```.
![image](https://assets.leetcode.com/users/votrubac/image_1562473681.png)
## C++ Solution
```
vector<int> corpFlightBookings(vector<vector<int>>& bookings, int n) {
  vector<int> res(n);
  for (auto &v : bookings) {
    res[v[0] - 1] += v[2];
    if (v[1] < n) res[v[1]] -= v[2];
  }
  for (auto i = 1; i < n; ++i) res[i] += res[i - 1];
  return res;
}
```
## Java Solution
```
public int[] corpFlightBookings(int[][] bookings, int n) {
  int[] res = new int[n];
  for (int[] v : bookings) {
    res[v[0] - 1] += v[2];
    if (v[1] < n) res[v[1]] -= v[2];
  }
  for (int i = 1; i < n; ++i) res[i] += res[i - 1];
  return res;
}
```
## Complexity Analysis
Runtime: *O(n)*, where n is the number of flights (or bookings).
Memory: *O(n)*
