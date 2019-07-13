In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1104.path-in-zigzag-labelled-binary-tree.algorithms.json

C++ O(log n)

https://leetcode.com/problems/path-in-zigzag-labelled-binary-tree/discuss/323293

* Lang:    python
* Author:  votrubac
* Votes:   29

# Intuition
If the tree is numbered left-to-right (not zigzag), the parent\'s label can be always determined as ```label / 2```. For zigzag, we need to "invert" the parent label.
# Solution
Determine the tree ```level``` where our value is located. The maximum label in the level is ```1 << level - 1```, and minimum is ```1 << (level - 1)```. We will use this fact to "invert" the parent label.
```
vector<int> pathInZigZagTree(int label, int level = 0) {
  while (1 << level <= label) ++level;
  vector<int> res(level);
  for(; label >= 1; label /= 2, --level) {
    res[level - 1] = label;
    label = (1 << level) - 1 - label + (1 << (level - 1));
  }
  return res;
}
```
# Complexity Analysis
Runtime: *O(log n)*
Memory: *O(1)* or *O(log n)* if we consider the memory required for the result.
