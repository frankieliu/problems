In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1134.armstrong-number.algorithms.json

Java Simple Solution

https://leetcode.com/problems/armstrong-number/discuss/345017

* Lang:    python
* Author:  anshu4intvcom
* Votes:   2

```
class Solution {
    public boolean isArmstrong(int N) {
        String str = String.valueOf(N);
        int n = str.length();
        int curr = 0;
        for(char c : str.toCharArray()) {
            curr += (int) Math.pow(c-\'0\', n);
        }
        return curr == N;
    }
}
```
