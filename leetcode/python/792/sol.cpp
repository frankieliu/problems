
c++ simple solution

https://leetcode.com/problems/number-of-matching-subsequences/discuss/250738

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

```
class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        auto res = 0;

        for (auto str: words) {
            auto i = 0;

            for (auto c: S) {
                if (c == str[i])
                    i++;
                if (i == str.length()) {
                    res++;
                    break;
                }
            }
        }

        return res;
    }
};
```
