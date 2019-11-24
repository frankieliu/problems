In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1128.number-of-equivalent-domino-pairs.algorithms.json

[Java/C++/Python] Easy and Concise

https://leetcode.com/problems/number-of-equivalent-domino-pairs/discuss/340022

* Lang:    python
* Author:  lee215
* Votes:   27

# **Intuition**
To count the number of same dominoes, I did it in this way:
For each domino `d`, calculate `min(d[0], d[1]) * 10 + max(d[0], d[1])`

This will put the smaller number on the left and bigger one on the right (in decimal).

Take the example from the problem:
`dominoes = [[1,2],[2,1],[3,4],[5,6]]`
now we transform it into `[12,12,34,56]`.
<br>

# **Explanation**
In solution 1, we sum up the pair in the end after the loop.
In solution 2, we sum up the pairs right away during the loop.
Almost the same idea.
<br>

# **Complexity**
Time `O(N)`
Space `O(N)`
<br>

# Solution 1
**Java:**
```java
    public int numEquivDominoPairs(int[][] dominoes) {
        Map<Integer, Integer> count = new HashMap<>();
        int res = 0;
        for (int[] d : dominoes) {
            int k = Math.min(d[0], d[1]) * 10 + Math.max(d[0], d[1]);
            count.put(k, count.getOrDefault(k, 0) + 1);
        }
        for (int v : count.values()) {
            res += v * (v - 1) / 2;
        }
        return res;
    }
```

**Python:**
```python
    def numEquivDominoPairs(self, A):
        return sum(v * (v - 1) / 2 for v in collections.Counter(tuple(sorted(x)) for x in A).values())
```
<br>

# Solution 2
**C++:**
```cpp
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        unordered_map<int, int> count;
        int res = 0;
        for (auto& d : dominoes) {
            res += count[min(d[0], d[1]) * 10 + max(d[0], d[1])]++;
        }
        return res;
    }
```

