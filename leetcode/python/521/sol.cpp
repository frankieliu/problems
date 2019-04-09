
C++ one line Solution

https://leetcode.com/problems/longest-uncommon-subsequence-i/discuss/99429

* Lang:    cpp
* Author:  yular
* Votes:   1

```
class Solution {
public:
    int findLUSlength(string a, string b) {
        return a == b?-1:max(a.size(), b.size());
    }
};
```
