In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1037.valid-boomerang.algorithms.json

[Java/C++/Python] Straight Forward

https://leetcode.com/problems/valid-boomerang/discuss/286702

* Lang:    python
* Author:  lee215
* Votes:   27

Assuming three points are A, B, C.

The first idea is that, calculate the area of ABC.
We can reuse the conclusion and prove in [812. Largest Triangle Area](https://leetcode.com/problems/largest-triangle-area/discuss/122711/C++JavaPython-Solution-with-Explanation-and-Prove)

The other idea is to calculate the slope of AB and AC.
`K_AB = (p[0][0] - p[1][0]) / (p[0][1] - p[1][1])`
`K_AC = (p[0][0] - p[2][0]) / (p[0][1] - p[2][1])`

We check if `K_AB != K_AC`, instead of calculate a fraction.

Time `O(1)` Space `O(1)`

<br>

**Java:**
```
    public boolean isBoomerang(int[][] p) {
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]);
    }
```

**C++:**
```
    bool isBoomerang(vector<vector<int>>& p) {
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1]);
    }
```

**Python:**
```
    def isBoomerang(self, p):
        return (p[0][0] - p[1][0]) * (p[0][1] - p[2][1]) != (p[0][0] - p[2][0]) * (p[0][1] - p[1][1])
```

