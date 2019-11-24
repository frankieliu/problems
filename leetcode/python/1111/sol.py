In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1111.maximum-nesting-depth-of-two-valid-parentheses-strings.algorithms.json

[Java/C++/Python] O(1) Extra Space Except Output

https://leetcode.com/problems/maximum-nesting-depth-of-two-valid-parentheses-strings/discuss/328841

* Lang:    python
* Author:  lee215
* Votes:   43

[Youtube](https://www.youtube.com/watch?v=_adniHPvQyE)
[Bilibili](https://www.bilibili.com/video/av58142681)
## Solution 0: Alternatively Distribute Parentheses
Basically, `(` is 1 point, `)` is `-1` point.
We try to keep total points of two groups even,
by distributing parentheses alternatively.

The good part of this solution is that,
we actually need no extra variable to record anything.


**Java:**
```java
    public int[] maxDepthAfterSplit(String seq) {
        int n = seq.length(), res[] = new int[n];
        for (int i = 0; i < n; ++i)
            res[i] = seq.charAt(i) == \'(\' ? i & 1 : (1 - i & 1);
        return res;
    }
```

**C++:**
```cpp
    vector<int> maxDepthAfterSplit(string seq) {
        vector<int> res(seq.length());
        for (int i = 0; i < seq.length(); ++i)
            res[i] = i & 1 ^ (seq[i] == \'(\');
        return res;
    }
```

**1-line Python:**
```python
    def maxDepthAfterSplit(self, seq):
        return [i & 1 ^ (seq[i] == \'(\') for i, c in enumerate(seq)]
```
<br>

# Complexity
Time `O(N)` for one pass
Space `O(1)` extra space,  `O(N)` for output
<br>

# More
Also provide some more easy understood ideas for this problem,
pick the the one you like.
(As I keep receiving complaints about the readability,
like no parentheses in solution for problem of parentheses)
<br>

# Solution 1: Keep Two Group Even
Count the number of open parentheses of group `A` and group `B`.
**Java:**
```java
    public int[] maxDepthAfterSplit(String seq) {
        int A = 0, B = 0, n = seq.length();
        int[] res = new int[n];
        for (int i = 0; i < n; ++i) {
            if (seq.charAt(i) == \'(\') {
                if (A < B) {
                    ++A;
                } else {
                    ++B;
                    res[i] = 1;
                }
            } else {
                if (A > B) {
                    --A;
                } else {
                    --B;
                    res[i] = 1;
                }
            }
        }
        return res;
    }
```

**C++:**
```cpp
    vector<int> maxDepthAfterSplit(string seq) {
        int A = 0, B = 0, n = seq.length();
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            if (seq[i] == \'(\') {
                if (A < B) ++A;
                else ++B, res[i] = 1;
            } else {
                if (A > B) --A;
                else --B, res[i] = 1;
            }
        }
        return res;
    }
```

**Python:**
```python
    def maxDepthAfterSplit(self, seq):
        A = B = 0
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            v = 1 if c == \'(\' else -1
            if (v > 0) == (A < B):
                A += v
            else:
                B += v
                res[i] = 1
        return res

```
<br>

# Solution 2: Split by Half
Count the number of level of whole string.
Then split it by half.
Group 0: the part under the half height
Group 1: the part above the half height

**Java:**
```java
    public int[] maxDepthAfterSplit(String seq) {
        int depth = 0, cur = 0, n = seq.length();
        for (int i = 0; i < n; ++i) {
            cur +=  seq.charAt(i) == \'(\' ?  1 : -1;
            depth = Math.max(depth, cur);
        }
        int[] res = new int[n];
        for (int i = 0; i < n; ++i) {
            if (seq.charAt(i) == \'(\') {
                if (++cur > depth / 2)
                    res[i] = 1;
            } else {
                if (cur-- > depth / 2)
                    res[i] = 1;
            }
        }
        return res;
    }
```

**C++:**
```cpp
    vector<int> maxDepthAfterSplit(string seq) {
        int depth = 0, cur = 0, n = seq.length();
        for (char c : seq)
            depth = max(depth, cur += c == \'(\' ? 1 : -1);
        vector<int> res(n, 0);
        for (int i = 0; i < n; ++i) {
            if (seq[i] == \'(\' && ++cur > depth / 2) res[i] = 1;
            if (seq[i] == \')\' && cur-- > depth / 2) res[i] = 1;
        }
        return res;
    }
```

**Python:**
```python
    def maxDepthAfterSplit(self, seq):
        depth = cur = 0
        for c in seq:
            if c == \'(\':
                cur += 1
                depth = max(depth, cur)
            else:
                cur -= 1
        half = depth / 2
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == \'(\':
                cur += 1
                if cur > half: res[i] = 1
            else:
                if cur > half: res[i] = 1
                cur -= 1
        return res
```

