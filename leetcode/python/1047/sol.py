In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1047.remove-all-adjacent-duplicates-in-string.algorithms.json

[Java/C++/Python] Stack Idea

https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/discuss/294893

* Lang:    python
* Author:  lee215
* Votes:   29

Keep a `res` as current result.
Loop on characters in the string `S` one by one.
If the next character is the same as the last in `res`, pop the last character from `res`.
Otherwise append the  the next character to the end of `res`.

**Java**
```
    public String removeDuplicates(String S) {
        int i = 0, n = S.length();
        char[] stack = new char[n];
        for (int j = 0; j < n; ++j)
            if (i > 0 && stack[i - 1] == S.charAt(j))
                --i;
            else
                stack[i++] = S.charAt(j);
        return new String(stack, 0, i);
    }
```

**C++**
```
    string removeDuplicates(string S) {
        string res = "";
        for (char& c : S)
            if (res.size() && c == res.back())
                res.pop_back();
            else
                res.push_back(c);
        return res;
    }
```

**Python**
```
    def removeDuplicates(self, S):
        res = []
        for c in S:
            if res and res[-1] == c:
                res.pop()
            else:
                res.append(c)
        return "".join(res)
```
**Python 1-line**
```
    def removeDuplicates(self, S):
        return reduce(lambda s, c: s[:-1] if s[-1] == c else s + c, S, "#")[1:]
```

