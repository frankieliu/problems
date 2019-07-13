In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1048.longest-string-chain.algorithms.json

[Java/Python] Concise DP

https://leetcode.com/problems/longest-string-chain/discuss/294890

* Lang:    python
* Author:  lee215
* Votes:   40

Sort the `words` by word\'s length. (also can appply bucket sort)
For each word, loop on all possible previous word with 1 letter missing.
If we have seen this previous word, update the longest chain for the current word.
Finally return the longest word chain.
<br>

**Python:**
```
    def longestStrChain(self, words):
        dp = {}
        for w in sorted(words, key=len):
            dp[w] = max(dp.get(w[:i] + w[i + 1:], 0) + 1 for i in xrange(len(w)))
        return max(dp.values())
```
<br>

**Java**
Equivalent in Java suggested by @noname_minion
```
    public int longestStrChain(String[] words) {
        Map<String, Integer> dp = new HashMap<>();
        Arrays.sort(words, (a, b)->a.length() - b.length());
        for (String word : words) {
            int max = 0;
            for (int i = 0; i < word.length(); ++i) {
                String prev = word.substring(0, i) + word.substring(i + 1);
                max = Math.max(max, dp.getOrDefault(prev, 0) + 1);
            }
            dp.put(word, max);
        }
        int res = 0;
        for (int v : dp.values()) {
            res = Math.max(res, v);
        }
        return res;
    }
```

**C++**
Equivalent in C++ suggested by @thebotman
```
class Solution {
    static bool compare(const string &s1, const string &s2) {
        return s1.length() < s2.length();
    }

public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), compare);
        unordered_map<string, int> dp;
        for (string w : words) {
            int maxi = 0;
            for (int i = 0; i < w.length(); i++) {
                string word = w.substr(0, i) + w.substr(i + 1);
                maxi = max(maxi, dp[word] + 1);
            }
            dp[w] = maxi;
        }
        int result = 0;
        for (auto m : dp) {
            result = max(result, m.second);
        }
        return result;
    }
};
```
