In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1143.longest-common-subsequence.algorithms.json

C++ with picture, O(nm)

https://leetcode.com/problems/longest-common-subsequence/discuss/348884

* Lang:    python
* Author:  votrubac
* Votes:   10

# Intuition
LCS is a well-known problem, and there are similar problems here:
- [1092. Shortest Common Supersequence](https://leetcode.com/problems/shortest-common-supersequence/)
- [1062. Longest Repeating Substring](https://leetcode.com/problems/longest-repeating-substring/)
- [516. Longest Palindromic Subsequence](https://leetcode.com/problems/longest-palindromic-subsequence/)

Bottom-up DP utilizes a matrix ```m``` where we track LCS sizes for each combination of ```i``` and ```j```. For ```m[i][j]```, if ```a[i] == b[j]```, then we add one to LCS for ```m[i - 1][j - i]```. Otherwise, we pick the largest value between ```m[i - 1][j]``` and ```m[i][j - 1]```.

This picture shows the populated matrix for ```"xabccde", "ace"``` test case.
![image](https://assets.leetcode.com/users/votrubac/image_1564691262.png)
# Solution
```
int longestCommonSubsequence(string &a, string &b) {
  vector<vector<short>> m(a.size() + 1, vector<short>(b.size() + 1));
  for (auto i = 1; i <= a.size(); ++i)
    for (auto j = 1; j <= b.size(); ++j)
      if (a[i - 1] == b[j - 1]) m[i][j] = m[i - 1][j - 1] + 1;
      else m[i][j] = max(m[i - 1][j], m[i][j - 1]);
  return m[a.size()][b.size()];
}
```
## Complexity Analysis
Runtime: O(nm), where n and m are the string sizes.
Memory: O(nm).
# Memory Optimization
You may notice that we are only looking one row up in the solution above. So, we just need to store two rows.
```
int longestCommonSubsequence(string &a, string &b) {
  if (a.size() < b.size()) return longestCommonSubsequence(b, a);
  vector<vector<short>> m(2, vector<short>(b.size() + 1));
  for (auto i = 1; i <= a.size(); ++i)
    for (auto j = 1; j <= b.size(); ++j)
      if (a[i - 1] == b[j - 1]) m[i % 2][j] = m[(i -1) % 2][j - 1] + 1;
      else m[i % 2][j] = max(m[(i - 1) % 2][j], m[i % 2][j - 1]);
  return m[a.size() % 2][b.size()];
}
```
## Complexity Analysis
Runtime: O(nm), where n and m are the string sizes.
Memory: O(min(n,m)).
