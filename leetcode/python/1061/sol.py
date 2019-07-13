In leetcode init
[TRACE] inited plugin: cookie.chrome
[TRACE] skipped plugin: lintcode
[TRACE] skipped plugin: leetcode.cn
[TRACE] inited plugin: retry
[TRACE] inited plugin: cache
[TRACE] inited plugin: company
[TRACE] inited plugin: solution.discuss
[DEBUG] cache hit: problems.json
[DEBUG] cache hit: 1061.lexicographically-smallest-equivalent-string.algorithms.json

Simple union find with a twist in union

https://leetcode.com/problems/lexicographically-smallest-equivalent-string/discuss/304313

* Lang:    python
* Author:  rocky1990
* Votes:   2

```
class Solution {
    
    private int[] parent = new int[26];
    
    public String smallestEquivalentString(String A, String B, String S) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0;i < parent.length;i++) parent[i] = i;
        for (int i = 0;i < A.length();i++) {
            char ch1 = A.charAt(i);
            char ch2 = B.charAt(i);
            union(ch1 - \'a\', ch2 - \'a\');
        }
        for (char ch:S.toCharArray()) {
            int p = find(ch - \'a\');
            sb.append((char) (p + \'a\'));
        }
        return sb.toString();
    }
    
    private void union(int ch1, int ch2) {
        int p1 = find(ch1);
        int p2 = find(ch2);
        if (p1 < p2) {
            parent[p2] = p1; 
        } else {
            parent[p1] = p2;
        }
        
    }
    
    private int find(int x) {
        if (parent[x] != x) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }                                                       
}
```
