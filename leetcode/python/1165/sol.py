In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1165.single-row-keyboard.algorithms.json

Python3 beats 100%

https://leetcode.com/problems/single-row-keyboard/discuss/366967

* Lang:    python
* Author:  justin801514
* Votes:   3

```
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        cur_index = 0
        time = 0
        for w in word:
            next_index = keyboard.index(w)
            time += abs(next_index - cur_index)
            cur_index = next_index
        return time
```
