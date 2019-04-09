
C++ 8ms solution

https://leetcode.com/problems/find-and-replace-pattern/discuss/244780

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

```
class Solution {
private:
    vector<vector<int>> gen_pattern(string s) {
        vector<vector<int>> res;

        for (auto i = 0; i < s.length(); i++) {
            auto j = 0;
            auto size = res.size();
            for (; j < size; j++)
                if (s[i] == s[res[j][0]])
                    res[j].push_back(i);
    
            if (j == size)
                res.push_back({i});
        }

        return res;
    }
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<vector<int>> pat;
        vector<string> res;
        
        pat = gen_pattern(pattern);
        for (auto word: words)
            if (pat == gen_pattern(word))
                res.push_back(word);


        return res;
    }
};
```
