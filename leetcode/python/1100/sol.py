In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1100.find-k-length-substrings-with-no-repeated-characters.algorithms.json

[Java/C++/Python] Sliding Window & Follow-UP & Follow-Down

https://leetcode.com/problems/find-k-length-substrings-with-no-repeated-characters/discuss/322928

* Lang:    python
* Author:  lee215
* Votes:   8

# O(N) Brute Force
The brute force would check all substring and we have `O(KS)` substrings.
But actually there are only 26 characters.
As a result, `K > 26` there won\'t be substring without repeated characters.
This turns the brute force into only `O(N)` time.

Here comes Python 1 line version.

**Python:**
```python
    def numKLenSubstrNoRepeats(self, S, K):
        return 0 if K > 26 else sum(len(set(S[i:i + K])) == K for i in xrange(n - K + 1))
```
<br>

# Follow-up
Problem: Find K-Length Substrings With No Repeated Characters
Solution: Brute Force

Your interviewer doesn\'t satisfy with your well-done "brute force",
and now he throws out his follow-up.

Follow-up: Find Substrings With No Repeated Characters
<br>

# **Intuition**
Substring leads to the idea of sliding windows.
(Now sure if it\'s called two pointers or what, but I keep saying that)

Honestly speaking, for the original problem,
I guess I would have used a counter of character,
if I hadn\'t miss the parameter `K`.

But in the fact, I was talking and somehow completely miss the parameter `K`.
So I wrote the follow-up directly at first time.
<br>

## **Explanation**
`i` is the start index of the substring,
`j` is the end index of the substring.
Slide the index `j`, while `S[j]` is in the current substring set,
we remove `A[i]` from the set and increment `i`.

`j - i + 1` is the maximum length of the no repeated substring ending at `S[j]`.
So there are `j - i + 1` no repeated substring ending at `S[j]`.
<br>

## **Complexity**
Time `O(N)` for sliding windows
Space `O(1)`, as `set.size <= 26`
<br>

**Java:**
```java
    public int numSubstrNoRepeats(String S, int K) {
        HashSet<Character> cur = new HashSet<>();
        int res = 0, i = 0;
        for (int j = 0; j < S.length(); ++j) {
            while (cur.contains(S.charAt(j)))
                cur.remove(S.charAt(i++));
            cur.add(S.charAt(j));
            res += j - i + 1;
        }
        return res;
    }
```

**C++:**
```cpp
    int numSubstrNoRepeats(string S, int K) {
        unordered_set<int> cur;
        int res = 0, i = 0;
        for (int j = 0; j < S.size(); ++j) {
            while (cur.count(S[j]))
                cur.erase(S[i++]);
            cur.insert(S[j]);
            res += j - i + 1;
        }
        return res;
    }
```

**Python**
```python
    def numSubstrNoRepeats(self, S, K):
        res, i = 0, 0
        cur = set()
        for j in xrange(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            res += j - i + 1
        return res
```

# Follow-Down
And If `j - i + 1 >= K`, among all these strings,
there one and only one no repeated substring,
whose length is `K`.

That turns back to our original problem.
<br>

**Java:**
```java
    public int numKLenSubstrNoRepeats(String S, int K) {
        HashSet<Character> cur = new HashSet<>();
        int res = 0, i = 0;
        for (int j = 0; j < S.length(); ++j) {
            while (cur.contains(S.charAt(j)))
                cur.remove(S.charAt(i++));
            cur.add(S.charAt(j));
            res += j - i + 1 >= K ? 1 : 0;
        }
        return res;
    }
```

**C++:**
```cpp
    int numKLenSubstrNoRepeats(string S, int K) {
        unordered_set<int> cur;
        int res = 0, i = 0;
        for (int j = 0; j < S.size(); ++j) {
            while (cur.count(S[j]))
                cur.erase(S[i++]);
            cur.insert(S[j]);
            res += j - i + 1 >= K;
        }
        return res;
    }
```

**Python**
```python
    def numKLenSubstrNoRepeats(self, S, K):
        res, i = 0, 0
        cur = set()
        for j in xrange(len(S)):
            while S[j] in cur:
                cur.remove(S[i])
                i += 1
            cur.add(S[j])
            res += j - i + 1 >= K
        return res
```
