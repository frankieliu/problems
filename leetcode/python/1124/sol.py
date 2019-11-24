In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1124.longest-well-performing-interval.algorithms.json

[Java/C++/Python] O(N) Solution, Life needs 996 and 669

https://leetcode.com/problems/longest-well-performing-interval/discuss/334565

* Lang:    python
* Author:  lee215
* Votes:   84

[Youtube](https://www.youtube.com/watch?v=Up8iyOrq-5Y) in Chinese.

## **Intuition**
If working hour > 8 hours, yes it\'s tiring day.
But I doubt if 996 is a well-performing interval.
Life needs not only 996 but also 669.
<br>

## **Explanation**
We starts with a `score = 0`,
If the working `hour > 8`, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total `score > 0`,
the whole interval has positive score,
so we set `res = i + 1`.

If the score is a new lowest score, we record the day by `seen[cur] = i`.
`seen[score]` means the first time we see the `score` is `seen[score]`th day.

We want a positive score, so we want to know the first occurrence of `score - 1`.
`score - x` also works, but it comes later than `score - 1`.
So the maximum interval is `i - seen[score - 1]`
<br>

## **Complexity**
Time `O(N)` for one pass.
Space `O(N)` in worst case if no tiring day.

<br>

**Java:**
```java
    public int longestWPI(int[] hours) {
        int res = 0, score = 0, n = hours.length;
        Map<Integer, Integer> seen = new HashMap<>();
        for (int i = 0; i < n; ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) {
                res = i + 1;
            } else {
                seen.putIfAbsent(score, i);
                if (seen.containsKey(score - 1))
                    res = Math.max(res, i - seen.get(score - 1));
            }
        }
        return res;
    }
```

**C++:**
```cpp
    int longestWPI(vector<int>& hours) {
        int res = 0, score = 0, n = hours.size();
        unordered_map<int, int> seen;
        for (int i = 0; i < n; ++i) {
            score += hours[i] > 8 ? 1 : -1;
            if (score > 0) {
                res = i + 1;
            } else {
                if (seen.find(score) == seen.end())
                    seen[score] = i;
                if (seen.find(score - 1) != seen.end())
                    res = max(res, i - seen[score - 1]);
            }
        }
        return res;
    }
```

**Python:**
```python
    def longestWPI(self, hours):
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res
```

