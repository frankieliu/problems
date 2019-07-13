In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1094.car-pooling.algorithms.json

C++/Java O(n) Thousand and One Stops

https://leetcode.com/problems/car-pooling/discuss/317611

* Lang:    python
* Author:  votrubac
* Votes:   31

# Intuition
Since we only have 1,001 ```stops```, we can just figure out how many people get it and out in each location. 
# Solution
Process all trips, adding passenger count to the start location, and removing it from the end location. After processing all trips, a positive value for the specific location tells that we are getting more passengers; negative - more empty seats. 

Finally, scan all stops and check if we ever exceed our vehicle capacity.
## C++
```
bool carPooling(vector<vector<int>>& trips, int capacity) {
  int stops[1001] = {};
  for (auto t : trips) stops[t[1]] += t[0], stops[t[2]] -= t[0];
  for (auto i = 0; capacity >= 0 && i < 1001; ++i) capacity -= stops[i];
  return capacity >= 0;
}
```
## Java
```
public boolean carPooling(int[][] trips, int capacity) {    
  int stops[] = new int[1001]; 
  for (int t[] : trips) {
      stops[t[1]] += t[0];
      stops[t[2]] -= t[0];
  }
  for (int i = 0; capacity >= 0 && i < 1001; ++i) capacity -= stops[i];
  return capacity >= 0;
}
```
# Complexity Analysis
Runtime: *O(n)*, where *n* is the number of trips. 
Memory: *O(m)*, where *m* is the number of stops.
