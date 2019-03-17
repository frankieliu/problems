
9 lines Python, 10 lines C++

https://leetcode.com/problems/word-break-ii/discuss/44169

* Lang:    python3
* Author:  StefanPochmann
* Votes:   65

`sentences(i)` returns a list of all sentences that can be built from the suffix `s[i:]`.

**Python:**

    def wordBreak(self, s, wordDict):
        memo = {len(s): ['']}
        def sentences(i):
            if i not in memo:
                memo[i] = [s[i:j] + (tail and ' ' + tail)
                           for j in range(i+1, len(s)+1)
                           if s[i:j] in wordDict
                           for tail in sentences(j)]
            return memo[i]
        return sentences(0)

**C++:**

    vector<string> wordBreak(string s, unordered_set<string>& wordDict) {
        unordered_map<int, vector<string>> memo {{s.size(), {""}}};
        function<vector<string>(int)> sentences = [&](int i) {
            if (!memo.count(i))
                for (int j=i+1; j<=s.size(); j++)
                    if (wordDict.count(s.substr(i, j-i)))
                        for (string tail : sentences(j))
                            memo[i].push_back(s.substr(i, j-i) + (tail=="" ? "" : ' ' + tail));
            return memo[i];
        };
        return sentences(0);
    }
