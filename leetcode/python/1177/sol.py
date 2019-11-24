In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1177.can-make-palindrome-from-substring.algorithms.json

[Java/Python 3] 3 codes each: prefix sum of counting characters first then compare

https://leetcode.com/problems/can-make-palindrome-from-substring/discuss/371849

* Lang:    python
* Author:  rock
* Votes:   39

According to the description and examples, we can deduce that the `rearrange` implies the input string `s` can be changed to any sequence to get `close` to a palindrome. Here `close` means least times of replacement of chars needed to become a palindrome after `rearranging` of `s`.

Obviously, any two same chars can be `rearranged` to be symmetric part of a palindrome, only the odd count of the chars we need to care. Therefore, when looping through the String `s`, we need to know if the count of each char in any prefix of the stirng `s` is odd or not by computing the corrsponding prefix sum, then the same information can be obtained for substring between any two given indices `i` and `j` by `prefixSum[j] - prefixSum[i]`.

Sum those chars with odd number of occurrences, and we only need to replace half of them to make all in symmetric pairs. Here is the brief description of my algorithm:

1. Compute the prefix sum by counting the number of chars in substring(0,1), substring(0, 2), ..., substring(0,n);
2. Use the difference of the prefix sums to get the the number of chars in substring(queries[i][0], queries[i][1]), count those do NOT in symmetric pairs, divided by 2, and compare it with queries[i][2].

**Method 1: count each char**

**Java**
```
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        List<Boolean> ans = new ArrayList<>(); 
        int[][] cnt = new int[s.length() + 1][26];
        for (int i = 0; i < s.length(); ++i) {
            cnt[i + 1] = cnt[i].clone(); // copy previous sum.
            ++cnt[i + 1][s.charAt(i) - \'a\'];
        }
        for (int[] q : queries) {
            int sum = 0; 
            for (int i = 0; i < 26; ++i) {
                sum += (cnt[q[1] + 1][i] - cnt[q[0]][i]) % 2;
            }
            ans.add(sum / 2 <= q[2]);
        }
        return ans;
    }
```

----

**Python 3**
```
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        cnt = [[0] * 26]
        for i, c in enumerate(s):
            cnt.append(cnt[i][:])
            cnt[i + 1][ord(c) - ord(\'a\')] += 1
        return [sum((cnt[hi + 1][i] - cnt[lo][i]) % 2 for i in range(26)) // 2 <= k for lo, hi, k in queries]
```

----

**Method 2: use true/false to mark odd/even of the count of each char, credit to @mfboulos**

**Java**
```
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        List<Boolean> ans = new ArrayList<>(); 
        boolean[][] odds = new boolean[s.length() + 1][26]; // odds[i][j]: within range [0...i) of s, if the count of (char)(j + \'a) is odd. 
        for (int i = 0; i < s.length(); ++i) {
            odds[i + 1] = odds[i].clone();
            odds[i + 1][s.charAt(i) - \'a\'] ^= true;
        }
        for (int[] q : queries) {
            int sum = 0; 
            for (int i = 0; i < 26; ++i) {
                sum += (odds[q[1] + 1][i] ^ odds[q[0]][i]) ? 1 : 0; // if the count of (char)(i + \'a\') in substring(q[0], q[1] + 1) is odd. 
            }
            ans.add(sum / 2 <= q[2]);
        }
        return ans;
    }
```

----

**Python 3**

```
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        odds = [[False] * 26]
        for i, c in enumerate(s):
            odds.append(odds[i][:])
            odds[i + 1][ord(c) - ord(\'a\')] ^= True
        return [sum(odds[hi + 1][i] ^ odds[lo][i] for i in range(26)) // 2 <= k for lo, hi, k in queries]  
```

----

**Method 3: use integer bit 0/1 to mark the even/odd of the count of each char**

The `32` bits in a Java `int` are enough to cover the odd/even of the counts of `26` English letters. Use only the 26 least significant bits in an `int`.

**Java**

```
    public List<Boolean> canMakePaliQueries(String s, int[][] queries) {
        List<Boolean> ans = new ArrayList<>(); 
        int[] odds = new int[s.length() + 1]; // odds[i]: within range [0...i) of s, the jth bit of odd[i] indicates even/odd of the count of (char)(j + \'a\'). 
        for (int i = 0; i < s.length(); ++i)
            odds[i + 1] = odds[i] ^ 1 << s.charAt(i) - \'a\';
        for (int[] q : queries)
            ans.add(Integer.bitCount(odds[q[1] + 1] ^ odds[q[0]]) / 2 <= q[2]); // odds[q[1] + 1] ^ odds[q[0]] indicates the count of (char)(i + \'a\') in substring(q[0], q[1] + 1) is even/odd.
        return ans;
    }
```

----

**Python 3**

```
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        odds = [False]
        for i, c in enumerate(s):
            odds.append(odds[i] ^ 1 << (ord(c) - ord(\'a\')))
        return [bin(odds[hi + 1] ^ odds[lo]).count(\'1\') // 2 <= k for lo, hi, k in queries]   
```

----

**Analysis:**

Time & space: O(S + Q), where S = s.length(), Q = queries.length.
