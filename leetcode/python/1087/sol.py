In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1087.brace-expansion.algorithms.json

Java DFS

https://leetcode.com/problems/brace-expansion/discuss/312361

* Lang:    python
* Author:  wushangzhen
* Votes:   4

```
class Solution {
    public String[] expand(String S) {
        TreeSet<String> set = new TreeSet<>();
        if (S.length() == 0) {
            return new String[]{""};
        } else if (S.length() == 1) {
            return new String[]{S};
        }
        if (S.charAt(0) == \'{\') {
            int i = 0;
            while (S.charAt(i) != \'}\') {
                i++;
            }
            String sub = S.substring(1, i);
            String[] subs = sub.split(",");
            String[] strs = expand(S.substring(i + 1));
            for (int j = 0; j < subs.length; j++) {
                for (String str : strs) {
                    set.add(subs[j] + str);
                }
            }
        } else {
            String[] strs = expand(S.substring(1));
            for (String str : strs) {
                set.add(S.charAt(0) + str);
            }
        }
        return set.toArray(new String[0]);
    }
}
```
