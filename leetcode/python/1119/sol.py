In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1119.remove-vowels-from-a-string.algorithms.json

[Java/Python] 1-Lines

https://leetcode.com/problems/remove-vowels-from-a-string/discuss/334140

* Lang:    python
* Author:  lee215
* Votes:   6

**Java, replace all vowels:**
```java
    public String removeVowels(String S) {
        return S.replaceAll("[aeiou]", "");
    }
```

**Python:**
```python
    def removeVowels(self, S):
        return "".join(c for c in S if c not in "aeiou")
```

