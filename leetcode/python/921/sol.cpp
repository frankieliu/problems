
C++ solution

https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/discuss/246976

* Lang:    cpp
* Author:  mark1990301
* Votes:   0

```
class Solution {
public:
    int minAddToMakeValid(string S) {
        stack<char> s;
        for (char c: S) {
            if (c == \')\' && s.size() > 0 && s.top() == \'(\') {
                    s.pop();
            } else
                s.push(c);
        }
        return s.size();
    }
};
```
