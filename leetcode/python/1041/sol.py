In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1041.robot-bounded-in-circle.algorithms.json

[Java/C++/Python] Let Chopper Help Explain

https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856

* Lang:    python
* Author:  lee215
* Votes:   77

I expect this problem to be medium problem.
![image](https://assets.leetcode.com/users/lee215/image_1557633739.png)

## **Intuition**
Let chopper help explain.
(Chopper from one piece, will let him go if illegal)

Starting at the origin and face north `(0,1)`,
after one sequence of `instructions`,
1. if chopper return to the origin, he\'s in an obvious circle.
2. if chopper finishes with face not towards north,
it will get back to the initial status in another one or three sequences.
<br>

## **Explanation**
`(x,y)` is the location of chopper.
`d[i]` is the direction he is facing.
`i = (i + 1) % 4` will turn right
`i = (i + 3) % 4` will turn left
Check the final status after `instructions`.
<br>

## **Complexity**
Time `O(N)`
Space `O(1)`

<br>

**Java:**
```
    public boolean isRobotBounded(String ins) {
        int x = 0, y = 0, i = 0, d[][] = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};
        for (int j = 0; j < ins.length(); ++j)
            if (ins.charAt(j) == \'R\')
                i = (i + 1) % 4;
            else if (ins.charAt(j) == \'L\')
                i = (i + 3) % 4;
            else {
                x += d[i][0]; y += d[i][1];
            }
        return x == 0 && y == 0 || i > 0;
    }
```

**C++:**
```
    bool isRobotBounded(string instructions) {
        int x = 0, y = 0, i = 0;
        vector<vector<int>> d = {{0, 1}, {1, 0}, {0, -1}, { -1, 0}};
        for (char & ins : instructions)
            if (ins == \'R\')
                i = (i + 1) % 4;
            else if (ins == \'L\')
                i = (i + 3) % 4;
            else
                x += d[i][0], y += d[i][1];
        return x == 0 && y == 0 || i > 0;
    }
```

**Python:**
```
    def isRobotBounded(self, instructions):
        x, y, dx, dy = 0, 0, 0, 1
        for i in instructions:
            if i == \'R\': dx, dy = dy, -dx
            if i == \'L\': dx, dy = -dy, dx
            if i == \'G\': x, y = x + dx, y + dy
        return (x, y) == (0, 0) or (dx, dy) != (0,1)
```

