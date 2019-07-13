In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1054.distant-barcodes.algorithms.json

C++ with picture, O(N)

https://leetcode.com/problems/distant-barcodes/discuss/299371

* Lang:    python
* Author:  votrubac
* Votes:   49

# Intuition
In the worst case, we can have ```(N + 1) / 2``` occurrences of the same barcode. This barcode needs to be placed in ```[0, 2, 4 ...]``` positions to avoid the repetition.
# Solution
1. Count occurrences of each barcode using a hash map
2. Use a set to sort barcodes by their number of occurrences
3. Starting from most frequent, fill even positions with barcodes
4. Then fill odd positions with remaining barcodes

![image](https://assets.leetcode.com/users/votrubac/image_1558849617.png)
```
vector<int> rearrangeBarcodes(vector<int>& b, int pos = 0) {
  unordered_map<int, int> m;
  set<pair<int, int>> s;
  for (auto n : b) ++m[n];
  for (auto it = begin(m); it != end(m); ++it) s.insert({ it->second, it->first });
  for (auto it = s.rbegin(); it != s.rend(); ++it) {
    for (auto cnt = 0; cnt < it->first; ++cnt, pos += 2) {
      if (pos >= b.size()) pos = 1;
      b[pos] = it->second;
    }
  }
  return b;
}
```
## Complexity Analysis
Runtime: *O(n log n)*, where *n* is the number of unique elements.
Memory: *O(n)*. We store unique elements in the map and set.
# O(N) Solution
Like [Jianwen](https://leetcode.com/1033051159/) observed below, we do not need to sort all unique elements, we just need to determine the most frequent one and fill it first. The rest can be filled in any order.

Since barcodes are limited to ```[1...10000]```, we can use an array instead of hash map to make it even faster.
```
vector<int> rearrangeBarcodes(vector<int>& b) {
  short m[10001] = {};
  short max_cnt = 0, max_n = 0, pos = 0;
  for (auto n : b) {
      max_cnt = max(max_cnt, ++m[n]);
      max_n = max_cnt == m[n] ? n : max_n;
  }
  for (auto i = 0; i <= 10000; ++i) {
    auto n = i == 0 ? max_n : i;
    while (m[n]-- > 0) {
        b[pos] = n;
        pos = pos + 2 < b.size() ? pos + 2 : 1;
    }
  }
  return b;
}
```
## Complexity Analysis
Runtime: *O(N)*, where *N* is the total number of elements.
Memory: *O(n)*, where *n* is the number of unique elements we track the count for.
