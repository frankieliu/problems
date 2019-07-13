In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1081.smallest-subsequence-of-distinct-characters.algorithms.json

C++ O(n), identical to #316

https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/discuss/308194

* Lang:    python
* Author:  votrubac
* Votes:   52

The solution is exactly the same as for [316. Remove Duplicate Letters](https://leetcode.com/problems/remove-duplicate-letters).

From the input string, we are trying to greedily build a monotonically increasing result string. If the next character is smaller than the back of the result string, we remove larger characters from the back **providing** there are more occurrences of that character **later** in the input string.
```
string smallestSubsequence(string s, string res = "") {
  int cnt[26] = {}, used[26] = {};
  for (auto ch : s) ++cnt[ch - \'a\'];
  for (auto ch : s) {
    --cnt[ch - \'a\'];
    if (used[ch - \'a\']++ > 0) continue;
    while (!res.empty() && res.back() > ch && cnt[res.back() - \'a\'] > 0) {
      used[res.back() - \'a\'] = 0;
      res.pop_back();
    }
    res.push_back(ch);
  }
  return res;
}   
```
## Complexity Analysis
Runtime: O(n). We process each input character no more than 2 times.
Memory: O(1). We need the constant memory to track up to 26 unique letters.
