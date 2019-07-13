In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1052.grumpy-bookstore-owner.algorithms.json

[Java] Sliding window.

https://leetcode.com/problems/grumpy-bookstore-owner/discuss/299230

* Lang:    python
* Author:  rock
* Votes:   26

1. Use a sliding window `win` to record the number of satisfied customers if grumpy technique used for `X` minutes. Update the value of `win` when the window is wider than `X`.
2. Use `satisfy` to record the number of satistified customers without grumpy technique.
3. by the end of iterations, `satisfy` + `max(win)` is the answer.

```
    public int maxSatisfied(int[] customers, int[] grumpy, int X) {
        int satisfy = 0, max = 0;
        for (int i = 0, win = 0; i < grumpy.length; ++i) {
            if (grumpy[i] == 0) { satisfy += customers[i]; }
            else { win += customers[i]; }
            if (i >= X) {
                win -= grumpy[i - X] * customers[i - X];
            }
            max = Math.max(win, max);
        }
        return satisfy + max;        
    }
```

**Analysis:**

Time: O(n), space: O(1), where n = grumpy.length;
