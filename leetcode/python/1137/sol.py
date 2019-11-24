In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1137.n-th-tribonacci-number.algorithms.json

[Java/C++/Python] Straight Forward

https://leetcode.com/problems/n-th-tribonacci-number/discuss/345236

* Lang:    python
* Author:  lee215
* Votes:   9

## **Explanation**
Calculate next element `d = a + b + c`,
let `(a,b,c) = (b,c,d)`.
Repeat this process `n - 2` times;

We can loop `n` times and return `i0`.
It can remove the special cases for `n < 2`.
But I did `n - 2` loop on purpose.
`i1` and `i2` will get overflow.
Though it won\'t throw an error in Java. Hardly say it\'s a right answer.

A possibly better solution is to start with the number before i0,i1,i2.
As I did in python,
`i[-2] = 1`
`i[-1] = 1`
`i[0] = 0`
Then it won\'t have this problem.

## **Complexity**
Time `O(N)`
Space `O(1)`

<br>

**Java:**
```java
    public int tribonacci(int n) {
        if (n < 2) return n;
        int a = 0, b = 1, c = 1, d;
        while (n-- > 2) {
            d = a + b + c;
            a = b;
            b = c;
            c = d;
        }
        return c;
    }
```

**C++:**
```cpp
    int tribonacci(int n) {
        if (n < 2) return n;
        int a = 0, b = 1, c = 1, d = a + b + c;
        while (n-- > 2) {
            d = a + b + c, a = b, b = c, c = d;
        }
        return c;
    }
```

**Python:**
```python
    def tribonacci(self, n):
        a, b, c = 1, 0, 0
        for _ in xrange(n): a, b, c = b, c, a + b + c
        return c
```

