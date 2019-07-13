In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1071.greatest-common-divisor-of-strings.algorithms.json

[Java] 3 codes: Recursive, iterative and regex w/ brief comments and analysis.

https://leetcode.com/problems/greatest-common-divisor-of-strings/discuss/303781

* Lang:    python
* Author:  rock
* Votes:   24

**Method 1: imitate gcd algorithm, recursive version.**

1. If longer string starts with shorter string, cut off the common prefix part of the longer string; repeat till one is empty, then the other is gcd string;
2. If the longer string does NOT start with the shorter one, there is no gcd string.

```
    public String gcdOfStrings(String str1, String str2) {
        if (str1.length() < str2.length()) { return gcdOfStrings(str2, str1); } // make sure str1 is not shorter than str2.
        else if (!str1.startsWith(str2)) { return ""; } // shorter string is not common prefix.
        else if (str2.isEmpty()) { return str1; } // gcd string found.
        else { return gcdOfStrings(str1.substring(str2.length()), str2); } // cut off the common prefix part of str1.
    }
```
**Analysis:**

Time cost of `startsWith()` and `substring()` is the total length of the longer strings during all recursion calls;

Worst case: str1 is `n` repeated `\'A\'`, str2 is `\'A\'`, and the time cost is as follows:
`1 + 2 + 3 + ... + n = n * (n + 1) / 2`.

space cost of `substring()`  is similar.

recursion stack space cost is minor part and can be ignored in space complexity analysis.

**Time & space:** `O(n ^ 2)`, where `n = max(str1.length(), str2.length())`.

---

**Method 2: compare substring, iterative version.**

the length of gcd substring must be the gcd of the lengthes of both string.

check if the `substring(0, i)` of `str1` is the divisor string of
1. `str1`;
2. `str2`.
Increase `i` to find its maximum value for gcd string.

```
    public String gcdOfStrings(String str1, String str2) {
        int i = 1, max = 0, len1 = str1.length(), len2 = str2.length();
        while (i <= len1 && i <= len2 && str1.charAt(i - 1) == str2.charAt(i - 1)) {
            boolean cd = true; // common divisor flag.
            if (len1 % i == 0 && len2 % i == 0) { // substring length i must be the common divisor of lengthes of str1 and str2.
                String commonDivisorStr = str1.substring(0, i);
                for (int j = 2 * i; cd && j <= len1; j += i) {
                    cd = commonDivisorStr.equals(str1.substring(j - i, j));
                }
                for (int j = 2 * i; cd && j <= len2; j += i) {
                    cd = commonDivisorStr.equals(str2.substring(j - i, j));
                }
                if (cd) max = i;
            }
            ++i;
        }
        return str1.substring(0, max);
    }
```
or make it simpler, credit to @Zzz_.

A common divisor must be prefix of the shorter string, and if `replace()` it in both strings, they end up with two empty strings.
```
    public String gcdOfStrings(String str1, String str2) {
        String s = str1.length() < str2.length() ? str1 : str2;
        for (int d = 1, end = s.length(); d <= end; ++d) {
            if (end % d != 0) { continue; } // only if length of s mod d is 0, can sub be common divisor.
            String sub = s.substring(0, end / d);
            if (str1.replace(sub, "").isEmpty() && str2.replace(sub, "").isEmpty()) {
                return sub;
            }
        }
        return "";
    }
```
---
**Method 3: Regular Expression.**

Start from the whole of `str1`, keep decreasing the right bound, till we find the gcd.
Note for regex:
1. `()` to make the string inside as a group;
2. `+` is quantifier, which means 1 or more of the group ahead of the `+`.
. 
```
import java.util.regex.Pattern;

    public String gcdOfStrings(String str1, String str2) {
        for (int i = str1.length(); i > 0; --i) {
            String gcd = str1.substring(0, i), ptn = "(" + gcd + ")+";
            if (Pattern.compile(ptn).matcher(str1).matches() && Pattern.compile(ptn).matcher(str2).matches()) {
                return gcd;
            }
        }
        return "";
    }
```
**Analysis:**

Time: O(n ^ 2), space: O(n), where n = max(str1.length(), str2.length()).
