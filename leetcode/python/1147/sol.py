In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1147.longest-chunked-palindrome-decomposition.algorithms.json

[Java/C++/Python] Easy Greedy with Prove

https://leetcode.com/problems/longest-chunked-palindrome-decomposition/discuss/350560

* Lang:    python
* Author:  lee215
* Votes:   38

## **Intuition**
Honestly I wrote a DP solution first, to ensure it get accepted.
Then I realized greedy solution is right.

Give a quick prove here.
If we have long prefix matched and a shorter prefix matched at the same time.
The longer prefix can always be divided in to smaller part.

![image](https://assets.leetcode.com/users/lee215/image_1564892108.png)

Assume we have a longer blue matched and a shorter red matched.
As definition of the statement, we have `B1 = B2, R1 = R4`.

Because `B1 = B2`,
the end part of `B1` = the end part of `B2`,
equal to `R2 = R4`,
So we have `R1 = R4 = R2`.

`B` is in a pattern of `R` + middle part + `R`.
Instead take a longer `B` with 1 point,
we can cut it in to 3 parts to gain more points.

This proves that greedily take shorter matched it right.
Note that the above diagram shows cases when `shorter length <= longer length/ 2`
When `shorter length > longer length/ 2`, this conclusion is still correct.
<br>

To be more general,
the longer prefix and shorter prefix will alway be in these patter:

`longer = a + ab * N`
`shorter = a + ab * (N - 1)`

for example:
longer = `"abc" + "def" + "abc"`
shorter = `"abc"`

for example:
longer = `"abc" * M`
shorter = `"abc" * N`
where `M > N`
<br>

## **Solution 1, very brute force**
When we know the greedy solution is right,
the coding is easier.
Just take letters from the left and right side,
Whenever they match, `res++`.
<br>

## **Complexity**
I just very brute force generate new string and loop the whole string.
Complexity can be improve on these two aspects.
Pardon that I choose the concise over the performance.

Time `O(N) * O(string)`
Space `O(N)`
<br>

**Java:**
```java
    public int longestDecomposition(String S) {
        int res = 0, n = S.length();
        String l = "", r = "";
        for (int i = 0; i < n; ++i) {
            l = l + S.charAt(i);
            r = S.charAt(n - i - 1) + r;
            if (l.equals(r)) {
                ++res;
                l = "";
                r = "";
            }
        }
        return res;
    }
```

**C++:**
```cpp
    int longestDecomposition(string S) {
        int res = 0, n = S.length();
        string l = "", r = "";
        for (int i = 0; i < n; ++i) {
            l = l + S[i], r = S[n - i - 1] + r;
            if (l == r)
                ++res, l = "", r = "";
        }
        return res;
    }
```

**Python:**
```python
    def longestDecomposition(self, S):
        res, l, r = 0, "", ""
        for i, j in zip(S, S[::-1]):
            l, r = l + i, j + r
            if l == r:
                res, l, r = res + 1, "", ""
        return res
```
<br>

## **Solution 2, Tail Recursion**
Same idea, just apply tail recursion.
And add a quick check before we slice the string.
<br>
**C++:**
```cpp
    int longestDecomposition(string S, int res = 0) {
        int n = S.length();
        for (int l = 1; l <= n / 2; ++l)
            if (S[0] == S[n - l] && S[l - 1] == S[n - 1])
                if (S.substr(0, l) == S.substr(n - l))
                    return longestDecomposition(S.substr(l, n - l - l), res + 2);
        return n ? res + 1 : res;
    }
```

**Python:**
```python
    def longestDecomposition(self, S, res=0):
        n = len(S)
        for l in xrange(1, n / 2 + 1):
            if S[0] == S[n - l] and S[l - 1] == S[n - 1]:
                if S[:l] == S[n - l:]:
                    return self.longestDecomposition(S[l:n - l], res + 2)
        return res + 1 if S else res
```
